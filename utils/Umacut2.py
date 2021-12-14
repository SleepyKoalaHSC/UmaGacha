from moviepy.editor import *
from moviepy.Clip import *
import os
import re
import cv2

fps = []
frame = [[0, 1405], [1385, 1556], [1575, 1740], [1738, 1908]]
path = r'H:\うまぴょい伝説\新建文件夹'
paths = []
output_clip = []

for root, dirs, files in os.walk(path):
    for file in files:
        paths.append(file)
        vidcap = cv2.VideoCapture(os.path.join(root, file))
        f = vidcap.get(cv2.CAP_PROP_FPS)
        fps.append(f)
file_fps_dict = dict(zip(paths, fps))
paths = sorted(paths, key=lambda i: int(re.match(r'(\d+)', i).group()))

for i in range(3):
    clip = VideoFileClip(path + '\\' + paths[i])
    clip = clip.subclip(frame[i][0] / file_fps_dict[paths[i]], frame[i][1] / file_fps_dict[paths[i]])
    if i == 0:
        output_clip = clip
    else:
        output_clip = concatenate_videoclips([output_clip, clip])

output_clip.write_videofile("demo.mp4")
