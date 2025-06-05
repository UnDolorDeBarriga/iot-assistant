#!/bin/bash
set -e

echo "Updating and installing dependencies..."
sudo apt update
sudo apt install -y python3-pip python3-venv portaudio19-dev mosquitto

echo "Creating Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing Python packages..."
pip install -r requirements.txt

echo "Downloading Vosk model if needed..."
mkdir -p models
cd models
if [ ! -d "vosk-model-small-en-us-0.15" ]; then
  wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip -O vosk.zip
  unzip vosk.zip && rm vosk.zip
fi
cd ..

echo "Done!"

