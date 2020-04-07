from pytube import YouTube 
import os
PATH=os.getcwd()

 
link="" #link here
yt = YouTube(link)
YouTube(link).streams.filter(file_extension='mp4').first().download(PATH)
print("saved")
