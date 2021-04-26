import youtube_dl
import subprocess

video = input("Enter video URL: ")
start_time = input("Time to start (in format hh:mm:ss.ms): \nNote that clip starts 30s after time entered \n")
vid_len = input("Length of clip (in format hh:mm:ss.ms): ")
filename = input("Filename: ")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    result = ydl.extract_info(video, download=False)
formats = result['formats']

x = 0
for i in formats:
     if formats[x]['ext'] == 'mp4' and formats[x]['height'] == 1080: #only downloads 1080p mp4 files
        vid_url = (formats[x]['url'])
     if formats[x]['ext'] == 'm4a':     #only downloads m4a audio files
         audio_url = (formats[x]['url'])
     x += 1
     
subprocess.run('ffmpeg -ss {} -i "{}" -ss {} -i "{}" -map 0:v -map 1:a -ss 30 -t {} -c:v libx264 -c:a aac {}.mp4'.format(start_time, vid_url, start_time, audio_url, vid_len, filename))
