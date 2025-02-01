import cv2
import os
from datetime import datetime

def capture_photo(save_dir):
    os.makedirs(save_dir, exist_ok=True)
    cam = cv2.VideoCapture(0)  # Open the default webcam (0)
    ret, frame = cam.read()
    if ret:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(save_dir, f"memory_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Photo saved: {filename}")
    cam.release()