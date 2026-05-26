#converting the videos to mp3 files
import os
import subprocess

files = os.listdir("videos")

for file in files:
    print("Processing:", file)
    video_path = os.path.join("videos", file)
    audio_name = os.path.splitext(file)[0] + ".mp3"
    audio_path = os.path.join("audios", audio_name)

    command = ["ffmpeg", "-i", video_path, audio_path]
    subprocess.run(command)
    print("All videos converted!")
   