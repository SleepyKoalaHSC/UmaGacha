import os
import re

path = '../static/movies/3stars/'

for root, dirs, files in os.walk(path):
    for file in files:
        newname = re.sub('\（.*?\）', '', file)
        os.rename(path+file, path+newname)
