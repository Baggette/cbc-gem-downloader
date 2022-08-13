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
while True:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        URL = input("Please enter the url to download from (You have to be signed into cbc gem): \n")
        ydl.download(URL)
        print("All files finished successfully!")
        dl_check = input("Would you like to download more files from cbc gem? y/n \n")
        if dl_check == "y" :
            continue
        else:
            print("Thanks for using my script! \n Bye")
            exit()
