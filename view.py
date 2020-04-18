from app import app, db
from flask import render_template, request, jsonify
from models import *
import json
import base64
from datetime import datetime


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/HeatMap_chengdu', methods=['POST'])
def homepage():
    # 用户登录判定
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter(User.username == username, User.password == password).all()
    if username == 'luosida':
        username = '罗嗣达'
    elif username == 'jiangrenkai':
        username = '姜人楷'
    elif username == 'xiangguangyu':
        username = '向广宇'
    else:
        username = '万斌朝硕'

    if not user:
        return "User's name and password are not correct! Please try again."
    else:
    # 加载成都市各区安全状态数据
        districtInfo = DistrictInfo.query.all()
        return render_template("start1.html",
                               username=username,
                               districtInfo = districtInfo)


if __name__ == '__main__':
    app.run()
