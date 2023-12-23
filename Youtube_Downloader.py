#To run in the terminal, use put in (zsh yt.sh "filename")

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title :", yt.title)

video = yt.streams.get_highest_resolution()
video.download('/Users/godfreyantomarlin/Downloads/Python_projects/Youtube_Downloader/Downloaded_Videos')

