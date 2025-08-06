# iot-assistant

## Setup (one time)

```bash
./scripts/setup.sh
```

```bash
python -m assistant.testing
python -m assistant.wakeword_test
python -m assistant.temp
```


```
arecord -l
```

Integrate wakeword + SST
    Start listen_and_transcribe() when wake word.
    TODO: Test listen_and_transcribe()

Command Parsing
    ONGOING

Publish MQTT
