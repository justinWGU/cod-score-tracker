import cv2
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent.parent 
DEFAULT_SCREENSHOT_PATH = BASE_DIR / 'core' / 'services' / 'static' / 'screenshot.jpg'

def take_screenshot(stream_url, frame=None, filename=DEFAULT_SCREENSHOT_PATH):
    print('Opening stream...')
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("Failed to open stream.")
        return False

    # if a starting frame was given, set the camera to that frame.
    if frame:
        print(f'Setting capture frame to {frame}')
        cap.set(propId=cv2.CAP_PROP_POS_FRAMES, value=frame)

    ret, image = cap.read()
    cap.release()

    if ret:
        if cv2.imwrite(filename, image):
            print(f"Screenshot saved.")
        else:
            print("Failed to save screenshot.")
        return True
    else:
        print("Failed to capture image.")
        return False