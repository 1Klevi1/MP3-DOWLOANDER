from pytube import YouTube 
import os
# where to save
SAVE_PATH = r'C:\Users\E-store\OneDrive\Desktop\Yotube video'
# link of the playlist
VIDEO_url=str(input('Type an URL: '))
#'https://youtu.be/ZIHwtaq_JSw'

try:
    yt = YouTube(VIDEO_url)
except:
        print("Connection Error") #to handle exception
        
     # filters out all the files with "mp4" extension
mp3files=  yt.streams.filter(only_audio=True).first()
try:
        #downloading the video in the prefered folder
        out_file =  mp3files.download(output_path=SAVE_PATH)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.") 
except:
    print("Some Error!")
print('Task Completed!')