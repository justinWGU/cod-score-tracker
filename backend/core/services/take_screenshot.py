import subprocess
import cv2
import os
from dotenv import load_dotenv

load_dotenv()

def get_stream_url(youtube_url):
    try:
        result = subprocess.run(
            ['yt-dlp', '-g', youtube_url],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Failed to extract stream URL:", e.stderr)
        return None

def take_screenshot_from_stream(stream_url, filename='static/screenshot.jpg'):
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("Failed to open stream.")
        return False

    ret, frame = cap.read()
    cap.release()

    if ret:
        cv2.imwrite(filename, frame)
        print(f"Screenshot saved as {filename}")
        return True
    else:
        print("Failed to capture frame.")
        return False


def take_screenshot():
    youtube_live_url = os.getenv("STREAM_URL")
    print("Extracting stream URL...")
    direct_stream_url = get_stream_url(youtube_live_url)

    if direct_stream_url:
        print("Capturing screenshot...")
        take_screenshot_from_stream(direct_stream_url)


# if __name__ == "__main__":
#     youtube_live_url = os.getenv("STREAM_URL")
#
#     print("Extracting stream URL...")
#     direct_stream_url = get_stream_url(youtube_live_url)
#
#     if direct_stream_url:
#         print("Capturing screenshot...")
#         take_screenshot_from_stream(direct_stream_url)