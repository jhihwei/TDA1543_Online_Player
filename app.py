from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask import render_template
from os import walk
import subprocess
import sys


app = Flask(__name__)
api = Api(app)
path = 'music'
ip = '0.0.0.0'
# if sys.platform == 'linux':
#     p1 = subprocess.Popen(['hostname', '-I'], stdout=subprocess.PIPE)
#     ip = subprocess.check_output(['awk', '{print $1}'],stdin=p1.stdout)
#     ip = ip.decode('utf-8')

def get_file_list():
    for root, dirs, files in walk(path):
        return files

@app.route('/play', methods=['GET'])
def play():
    name = request.args.get('name')
    name = name[1:-1]
    subprocess.run(['ffmpeg', '-i', f'{path}/{name}','-f', 'alsa', 'hw:0,0'])
    return 'singing'


@app.route('/')
def index():
    return render_template('index.html', files=get_file_list(), ip=ip)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)