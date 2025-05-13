import cv2
from datetime import datetime
import paho.mqtt.client as mqtt

# Change this to your Mac's IP address
VIDEO_STREAM_URL = "http://192.168.100.118:5050/video"
MQTT_BROKER = "localhost"
MQTT_TOPIC = "edge/events"

def detect_motion(prev, curr, threshold=20):
    diff = cv2.absdiff(prev, curr)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=2)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours) > 0

# Init MQTT
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER)

print(f"🎥 Connecting to video stream at {VIDEO_STREAM_URL}")
cap = cv2.VideoCapture(VIDEO_STREAM_URL)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

if not ret:
    raise RuntimeError("❌ Could not read from video stream")

print("✅ Video stream opened, running motion detection...")

while cap.isOpened():
    if detect_motion(frame1, frame2):
        now = datetime.now().isoformat()
        print(f"⚠️ Motion detected at {now}")
        mqtt_client.publish(MQTT_TOPIC, f"motion detected at {now}")

    frame1, frame2 = frame2, cap.read()[1]
    if frame2 is None:
        break

cap.release()
