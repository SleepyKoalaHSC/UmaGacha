from moviepy.editor import *

path = r'D:\Projects\UmaGacha\static\movies\3stars\1.mp4'
clip = VideoFileClip(path)
clip.crop(x1=208, y1=0, x2=605, y2=720).write_videofile('out.mp4')
