import cv2
from video.stream_reader import open_stream
from ai.motion_detector import detect_motion
from comm.mqtt_publisher import MQTTPublisher

url = "http://<your_mac_ip>:5000/video"
cap = open_stream(url)
mqtt = MQTTPublisher()

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    if detect_motion(frame1, frame2):
        print("Motion detected")
        mqtt.publish("motion")

    frame1, frame2 = frame2, cap.read()[1]
    if frame2 is None:
        break

cap.release()

