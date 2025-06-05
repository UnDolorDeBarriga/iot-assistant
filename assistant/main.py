from dotenv import load_dotenv
import os

# Load config file
load_dotenv(dotenv_path="config/settings.env")

# Access config variables
mqtt_host = os.getenv("MQTT_HOST", "localhost")
mqtt_port = int(os.getenv("MQTT_PORT", "1883"))
mqtt_user = os.getenv("MQTT_USER", None)
mqtt_pass = os.getenv("MQTT_PASS", None)

print(f"[INFO] Connecting to MQTT broker at {mqtt_host}:{mqtt_port} as {mqtt_user or 'anonymous'}")

# Example usage with paho-mqtt
import paho.mqtt.client as mqtt

client = mqtt.Client()
if mqtt_user and mqtt_pass:
    client.username_pw_set(mqtt_user, mqtt_pass)

client.connect(mqtt_host, mqtt_port)
client.loop_start()

# Your logic here — wake word loop, etc.
