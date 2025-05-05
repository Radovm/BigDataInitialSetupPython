import cv2

def open_stream(url):
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        raise RuntimeError(f"Unable to open stream: {url}")
    return cap
