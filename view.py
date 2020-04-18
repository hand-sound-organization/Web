from app import app, db
from flask import render_template, request, jsonify
from models import *
import json
import base64


@app.route('/')
def login():
    print('xxxxxxxxxxxxxxxxxxxx')
    return render_template("login.html")


@app.route('/HeatMap_chengdu', methods=['POST'])
def homepage():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter(User.username == username, User.password == password).all()
    if not user:
        return "User's name and password are not correct! Please try again."
    else:
        return render_template("start1.html", username=username)


if __name__ == '__main__':
    app.run()
