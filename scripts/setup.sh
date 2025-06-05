#!/bin/bash
set -e

echo "Updating and installing dependencies..."
sudo apt update
sudo apt install -y python3-pip portaudio19-dev mosquitto

echo "Installing Python packages..."
pip3 install -r requirements.txt

echo "Downloading Vosk model if needed..."
mkdir -p models
cd models
if [ ! -d "vosk-model-small-en-us-0.15" ]; then
  wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip -O vosk.zip
  unzip vosk.zip && rm vosk.zip
fi
cd ..

echo "Done!"
