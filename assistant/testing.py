from assistant.parser import build_parser
from assistant.sst import transcribe_from_audio

# from assistant.sst import listen_and_transcribe

# for text in listen_and_transcribe():
#     print(f"[MAIN] Received: {text}")

def transcribe():
    for text in transcribe_from_audio("audios_test/close_lights.wav", reduce_noise=True):
        print("[RESULT]", text, "with noise reduction")

def test_transcribe():
    for text in transcribe_from_audio("audios_test/close_lights.wav", reduce_noise=True):
        print("[RESULT]", text, "with noise reduction")

    for text in transcribe_from_audio("audios_test/close_lights.wav", reduce_noise=False):
        print("[RESULT]", text, "without noise reduction")

    for text in transcribe_from_audio("audios_test/open_door.wav", reduce_noise=True):
        print("[RESULT]", text, "with noise reduction")

    for text in transcribe_from_audio("audios_test/open_door.wav", reduce_noise=False):
        print("[RESULT]", text, "without noise reduction")

def parser(text):
    parser = build_parser()
    for intent in parser.determine_intent(text):
        print("[INTENT] Parsed:", intent)

if __name__ == "__main__":
    parser("turn on the light")
