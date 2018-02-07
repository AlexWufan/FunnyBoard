from flask import Flask
from flask import render_template

from flask import Flask, session, request, redirect, url_for, render_template, abort, jsonify
import sqlite3 as lite
from flask import make_response


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/marker')
def maker():
    return render_template('marker.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.run()
