from app import app, db
from flask import render_template, request, jsonify, redirect, url_for, session, flash
from models import *
import random
import json
import base64
from datetime import datetime


# 用户登录
@app.route('/')
def login():
    return render_template("login.html")


# 用户登录判定
@app.route('/judgement', methods=['POST'])
def judgement():
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
        flash("Name or Password of user are not correct! Please try again.")
        return redirect(url_for('login'))
    else:
        session['user_name'] = username
        session['login_time'] = datetime.now()
        return redirect(url_for('homepage',
                                username=username
                                ))


# 成都市热力图展示页面
@app.route('/HeatMap_chengdu')
def homepage():
    # 加载成都市各区安全状态数据
    districtInfo = DistrictInfo.query.all()
    if session.get('user_name'):
        return render_template("start1.html",
                               username=session.get('user_name'),
                               districtInfo=districtInfo)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


# 热力图数据交互处理（获取热力图数据）
@app.route('/HeatMap_chengdu/data', methods=['POST'])
def homepage_data():
    pointdist = {"heatmapData": []}
    points = CityHeatMap.query.all()
    for point in points:
        pointdist["heatmapData"].append(json.dumps({
            "lng": point.lng - 12.4,
            "lat": point.lat - 9.3,
            "count": point.count
        }))
    heatmap_jsondata = json.dumps(pointdist)
    return jsonify(heatmap_jsondata)


# 热点图
@app.route('/HeatMap_chengdu/HeatPointMap')
def heatpoint():
    return render_template("start2.html")


@app.route('/HeatMap_chengdu/Advise')
def advise():
    return render_template("advise.html")


@app.route('/HeatMap_chengdu/Attacklog')
def attacklog():
    return render_template("attackLog.html")


@app.route('/HeatMap_chengdu/wuhou')
def wuhou():
    return render_template("area1.html")


@app.route('/HeatMap_chengdu/jinjiang')
def jinjiang():
    return render_template("area2.html")


@app.route('/HeatMap_chengdu/qinyang')
def qinyang():
    return render_template("area3.html")


@app.route('/HeatMap_chengdu/jinniu')
def jinniu():
    return render_template("area4.html")


@app.route('/HeatMap_chengdu/chenghua')
def chenghua():
    return render_template("area5.html")


@app.route('/HeatMap_chengdu/longquanyi')
def longquanyi():
    return render_template("area6.html")


@app.route('/HeatMap_chengdu/wenjiang')
def wenjiang():
    return render_template("area7.html")


@app.route('/HeatMap_chengdu/xindu')
def xindu():
    return render_template("area8.html")


@app.route('/HeatMap_chengdu/qinbaijiang')
def qinbaijiang():
    return render_template("area9.html")


@app.route('/HeatMap_chengdu/shuangliu')
def shuangliu():
    return render_template("area10.html")


@app.route('/HeatMap_chengdu/pidu')
def pidu():
    return render_template("area11.html")


if __name__ == '__main__':
    app.run()
