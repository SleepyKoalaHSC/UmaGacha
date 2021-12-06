import os
import subprocess
from flask import Flask
from moviepy.editor import CompositeVideoClip, VideoFileClip, concatenate_videoclips
import config.config as configs

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/movieList')
def movie_list():
    return '''
    <!DOCTYPE html>
<html>
<body>
<video width="400" height="300" controls="controls">
  <source src="static/movies/3stars/output.mp4" type="video/mp4" />
</video>
</body>
</html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
