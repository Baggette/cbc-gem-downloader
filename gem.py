import os
import yt_dlp
from dotenv import load_dotenv

load_dotenv()
ydl_opts = {
    "username": os.getenv("EMAIL"),
    "password": os.getenv("PASSWORD"),
    "overwrites": os.getenv("OVERWRITES"),
    "cookies-from-browser": os.getenv("BROWSER"),
    "final_ext":"mp4",
    "format":'bestvideo[height<=' + str(os.getenv("VIDEO_HEIGHT")) + ']+bestaudio',
    "paths":{"home": os.getenv("OUTPUT_FOLDER")}
}
print("Please enter the url to download from (You have to be signed into cbc gem):")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    URL = input()
    info = ydl.extract_info(URL, download=False)
    ydl.download(URL)
