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
        URL = input("The URL for the show will determine which episode or season will be downloaded. \n eg: https://gem.cbc.ca/showname/s01e01 s is season e is episode number \n so if you wanted just season 2 it would be https://gem.cbc.ca/showname/s02 \n Please enter the url to download from (You have to be signed into cbc gem): ")
        ydl.download(URL)
        print("All files finished successfully!")
        dl_check = input("Would you like to download more files from cbc gem? y/n \n")
        if dl_check == "y" :
            continue
        else:
            print("Thanks for using my script!")
            input("Press enter to exit...")
            exit()
