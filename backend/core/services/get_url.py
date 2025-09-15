import subprocess

def get_url(youtube_url):
    print(f"Extracting direct URL from {youtube_url}...")
    result = subprocess.run(
        ['yt-dlp', '-g', '-f', 'bestvideo[ext=mp4][protocol!=m3u8]', youtube_url],
            capture_output=True,
            text=True,
            check=True
        )
    print('Direct url extracted...')
    return result.stdout.strip().split("\n")[0]