from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import LoginForm
from flask_wtf.csrf import CsrfProtect
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user
from models import User
import json

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
Bootstrap(app)

# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

# 这个callback函数用于reload User object，根据session中存储的user id
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# csrf protection
csrf = CsrfProtect()
csrf.init_app(app)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = request.form.get('username', None)
        password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        user = User(user_name, password)
        if user.verify_password(password):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main'))
    return render_template('login.html', title="Sign In", form=form)

@app.route('/')
def hello_world():
    return render_template('index.html')


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
