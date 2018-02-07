from flask import Flask
from flask import render_template
import json
import os


with open('/Users/Ziwen/PycharmProjects/FunnyBoard/data.json', 'r') as f:
    a = json.load(f)


app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/marker')
def maker():
    return render_template('marker.html')

@app.route('/1')
def test1():
    return render_template('1.html')

@app.route('/data')
def data():
    return json.dumps(a)

if __name__ == '__main__':
    app.run()
