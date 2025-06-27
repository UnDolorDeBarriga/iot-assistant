# from assistant.sst import listen_and_transcribe

# for text in listen_and_transcribe():
#     print(f"[MAIN] Received: {text}")

from assistant.sst import transcribe_from_audio

for text in transcribe_from_audio("audios_test/hello.wav", reduce_noise=True):
    print("[RESULT]", text, "with noise reduction")

for text in transcribe_from_audio("audios_test/hello.wav", reduce_noise=False):
    print("[RESULT]", text, "without noise reduction")

for text in transcribe_from_audio("audios_test/close_lights.wav", reduce_noise=True):
    print("[RESULT]", text, "with noise reduction")

for text in transcribe_from_audio("audios_test/close_lights.wav", reduce_noise=False):
    print("[RESULT]", text, "without noise reduction")

for text in transcribe_from_audio("audios_test/open_door.wav", reduce_noise=True):
    print("[RESULT]", text, "with noise reduction")

for text in transcribe_from_audio("audios_test/open_door.wav", reduce_noise=False):
    print("[RESULT]", text, "without noise reduction")