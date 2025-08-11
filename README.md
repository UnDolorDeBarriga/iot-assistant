# IoT Assistant (Raspberry Pi)

Voice-activated IoT assistant for Raspberry Pi. Listens for a wake word ("Hey Assistant"), transcribes a single command, parses intent, and publishes actions to MQTT.

## Requirements

- Raspberry Pi with Raspberry Pi OS (Debian-based)
- USB microphone (required)
- Internet connection and sudo access
- Picovoice access key for wake-word detection (free account)

## Quick Start

1) Clone the repository on the Raspberry Pi

```bash
git clone https://github.com/UnDolorDeBarriga/iot-assistant.git
cd iot-assistant
chmod +x scripts/*.sh
```

2) One-time setup (installs system packages, Python deps, Vosk models, and configures Mosquitto)

```bash
./scripts/setup.sh
```

3) Configure

- MQTT: copy the example env file and update values

```bash
cp config/settings.env.example config/settings.env
# edit config/settings.env and set MQTT_HOST, MQTT_PORT, MQTT_USER, MQTT_PASS
```

- Wake word: set your Picovoice access key. Create a file named `.env` in the project root or export it in your shell:

```bash
# Option A: project .env file
printf "PICOVOICE_ACCESS_KEY=YOUR_KEY_HERE\n" > .env

# Option B: export in shell (for current session)
export PICOVOICE_ACCESS_KEY=YOUR_KEY_HERE
```

- Audio: verify that the USB mic is detected (optional)

```bash
arecord -l
```

4) Run the assistant (use every time)

```bash
./scripts/run.sh
```

Press Ctrl+C to stop.

## Notes

- `setup.sh` uses sudo to install and enable the Mosquitto broker and creates a default `admin/admin` user. Adjust `config/mosquitto/mosquitto.conf` as needed.
- `run.sh` starts Mosquitto if not running, activates the virtual environment, and launches `assistant.main`.
- Wake word model path: `models/Hey-Assistant.ppn` (already included). Speech recognition uses Vosk models downloaded during setup.
- MQTT topics/payloads depend on parsed intents and are published by `assistant/mqtt_client.py`.
