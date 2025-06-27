import os
import noisereduce as nr
import numpy as np
import queue
import sounddevice as sd
import vosk
import json
import wave

model_path = "models/vosk-model-small-en-us-0.15"

if not os.path.exists(model_path):
    raise FileNotFoundError("Vosk model not found in models/. Run setup.sh first.")

model = vosk.Model(model_path)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(f"[AUDIO WARNING] {status}")
    q.put(bytes(indata))

def listen_and_transcribe():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("[STT] Listening...")
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"[STT] You said: {text}")
                    yield text

def transcribe_from_audio(file_path, reduce_noise=True):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    with wave.open(file_path, "rb") as wf:
        if wf.getframerate() != 16000 or wf.getnchannels() != 1:
            raise ValueError("Audio must be mono and 16kHz.")
        
        audio_data = wf.readframes(wf.getnframes())
        audio_np = np.frombuffer(audio_data, dtype=np.int16)

        if reduce_noise:
            print("[STT] Applying noise reduction...")
            audio_np = nr.reduce_noise(y=audio_np, sr=16000)

        audio_bytes = audio_np.astype(np.int16).tobytes()

        rec = vosk.KaldiRecognizer(model, 16000)
        rec.AcceptWaveform(audio_bytes)
        result = json.loads(rec.FinalResult())
        text = result.get("text", "")
        if text:
            yield text