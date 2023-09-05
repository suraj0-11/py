import os
from pytube import YouTube

url = input("Enter the YouTube video URL: ")
video = YouTube(url)
streams = video.streams.filter(progressive=True)
for i in range(len(streams)):
    print(f"{i+1}. Resolution: {streams[i].resolution}")
choice = int(input("Enter the number of the resolution you want to download: "))
stream = streams[choice-1]
download_dir = os.path.join(os.path.expanduser("~"), "Desktop")
stream.download(download_dir)