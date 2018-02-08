from flask import Flask
from flask import render_template
import json

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/marker')
# def maker():
#     # with app.open_resource('data.json', 'r') as f:
#     #     data = json.load(f)
#     with open('/Users/Ziwen/PycharmProjects/FunnyBoard/data.json', 'r') as f:
#         data = json.load(f)
#     return render_template('marker.html', data = json.dumps(data))

@app.route('/1')
def test1():
    with app.open_resource('data2.json', 'r') as f:
        data = json.load(f)
    return render_template('1.html', data = data)

# @app.route('/data')
# def data():
#     with app.open_resource('data.json', 'r') as f:
#         data = json.load(f)
#     return json.dumps(data)

if __name__ == '__main__':
    app.run()
