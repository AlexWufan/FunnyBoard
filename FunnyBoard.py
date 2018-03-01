from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import LoginForm
import json

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)

@app.route('/register')
def register():
    return render_template('register.html')

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
    return render_template('1.html', data=data)

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    with app.open_resource('data2.json', 'r') as f:
        data = json.load(f)

    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        action_type = request.form['action_type']
        cordinates = request.form['cordinates']
        cordinates = [float(cordinates.split(',')[0]), float(cordinates.split(',')[1])]
        new_feature = {
                          "type": "Feature",
                          "geometry": {
                              "type": "Point",
                              "coordinates": cordinates
                          },
                          "properties": {
                              "title": title,
                              "type": action_type,
                              "message": message
                          }
                      }

        data['features'].append(new_feature)

        with open('/Users/Ziwen/PycharmProjects/FunnyBoard/data2.json', 'w') as f:
            json.dump(data, f)

    return render_template('1.html', data=data)


# @app.route('/data')
# def data():
#     with app.open_resource('data.json', 'r') as f:
#         data = json.load(f)
#     return json.dumps(data)

if __name__ == '__main__':
    app.run()
