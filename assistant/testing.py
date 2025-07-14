from assistant.parser import build_parser
from assistant.sst import transcribe_from_audio
from assistant.sst import listen

def test_transcribe():
    for text in transcribe_from_audio("audios_test/close_lights.wav", reduce_noise=True):
        print("[RESULT]", text, "with noise reduction")

    for text in transcribe_from_audio("audios_test/close_lights.wav", reduce_noise=False):
        print("[RESULT]", text, "without noise reduction")

    for text in transcribe_from_audio("audios_test/open_door.wav", reduce_noise=True):
        print("[RESULT]", text, "with noise reduction")

    for text in transcribe_from_audio("audios_test/open_door.wav", reduce_noise=False):
        print("[RESULT]", text, "without noise reduction")

if __name__ == "__main__":
    listen()
    
