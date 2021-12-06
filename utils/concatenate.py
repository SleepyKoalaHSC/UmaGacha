import os
import subprocess

# path = r'D:\Projects\UmaGacha\static\movies\3stars'
# L = []
# for root, dirs, files in os.walk(path):
#     for file in files:
#         L.append(os.path.join(root, file))
#
# with open('1.txt', 'w', encoding='utf-8') as f:
#     for file in L:
#         line = 'file \'' + file + '\'\n'
#         f.write(line)

filelist = r'D:\Projects\UmaGacha\static\movies\3stars\1.txt'
cmd = 'ffmpeg -f concat -safe 0 -i %s -c copy -movflags +faststart output.mp4' % (filelist)
subprocess.call(cmd, shell=True)
