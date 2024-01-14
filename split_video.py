from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from moviepy.audio.fx.all import volumex

from sys import argv

# Replace the filename below.
required_video_file = argv[1]

target_video_file = required_video_file.replace(".mp4", "_{}.mp4")

video = VideoFileClip(required_video_file)
if len(argv) >= 3 and argv[2]:
    video = video.volumex(3)
    video.write_videofile("test.mp4")
video_duration = video.duration

stride = 720  # 600s = 10m
overlap = 5 # 5s video overlap
n_chunks = int(video_duration // stride + 1)

print(video_duration)
print(n_chunks)

starts = [(i * stride) - overlap for i in range(n_chunks)]
print(starts)

for i, start in enumerate(starts):
    ffmpeg_extract_subclip(required_video_file, start, start + stride, targetname=target_video_file.format(i))
