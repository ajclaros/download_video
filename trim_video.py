from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import argparse

parser = argparse.ArgumentParser(description='Trims video acording to frames')

parser.add_argument('--input_file', type=str,  help='the video file you want modified')
parser.add_argument('--start_time', type=str, help='where you want the new clip to start')
parser.add_argument('--end_time', type=str,  help='the video file you want modified')

args = parser.parse_args()
file = args.input_file
filename=file[:-4]
t1 = int(args.start_time)
t2 = int(args.end_time)

ffmpeg_extract_subclip(file, t1, t2, targetname=f"{filename}_{t1}_{t2}.mp4")

