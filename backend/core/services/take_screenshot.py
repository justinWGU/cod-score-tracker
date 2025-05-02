import subprocess
import cv2
import os
from dotenv import load_dotenv

load_dotenv()

def get_url(youtube_url):
    print(f"Extracting stream URL from {youtube_url}...")
    try:
        result = subprocess.run(
            ['yt-dlp', '-g', youtube_url],
            capture_output=True,
            text=True,
            check=True
        )
        print('Stream url extracted...')
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Failed to extract stream URL:", e.stderr)
        return None

# TODO: change fixed directory
def take_screenshot(stream_url, frame=None, filename='/Users/justin/projects/score-tracker/backend/core/services/static/screenshot.jpg'):
    print("Capturing screenshot...")
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("Failed to open stream.")
        return False

    # if a starting frame was given, set the camera to that frame.
    if frame:
        cap.set(propId=cv2.CAP_PROP_POS_FRAMES, value=frame)
        print(f"Rendering frame {frame}")

    ret, frame = cap.read()
    cap.release()

    if ret:
        if cv2.imwrite(filename, frame):
            print(f"Screenshot saved.")
        else:
            print("Failed to save screenshot.")
        return True
    else:
        print("Failed to capture frame.")
        return False


if __name__ == "__main__":

    print("taking screen shot...")
    youtube_live_url = os.getenv("STREAM_URL")


    print("Extracting stream URL...")
    direct_stream_url = get_url(youtube_live_url)

    if direct_stream_url:
        print("Capturing screenshot...")
        take_screenshot(direct_stream_url)