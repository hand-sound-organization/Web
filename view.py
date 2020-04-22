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
    if session.get('user_name'):
        districtInfo = DistrictInfo.query.all()
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
    if session.get('user_name'):
        districtInfo = DistrictInfo.query.all()
        return render_template("start2.html",
                               username=session.get('user_name'),
                               districtInfo=districtInfo)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/Advise')
def advise():
    if session.get('user_name'):
        return render_template("advise.html",
                               username=session.get('user_name'))
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/Attacklog')
def attacklog():
    if session.get('user_name'):
        return render_template("attackLog.html",
                               username=session.get('user_name'))
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/Attacklog/data', methods=['POST'])
def attacklog_data():
    logdist = {"attackLogData": []}
    loglist = AttackLog.query.all()
    for log in loglist:
        logdist["attackLogData"].append({
            "id": log.id,
            "lock_id": log.lock_id,
            "attack_time": str(log.attack_time),
            "lng": log.lng,
            "lat": log.lat,
            "isSafe": log.isSafe
        })
    log_jsondata = json.dumps(logdist)
    return jsonify(log_jsondata)


@app.route('/HeatMap_chengdu/changeInfo')
def changeInfo():
    if session.get('user_name'):
        return render_template("changeInfo.html",
                               username=session.get('user_name'))
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/wuhou')
def wuhou():
    if session.get('user_name'):
        area = '武侯区'
        areaList = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang', 'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/jinjiang')
def jinjiang():
    if session.get('user_name'):
        area = '锦江区'
        areaList = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/qinyang')
def qinyang():
    if session.get('user_name'):
        area = '青羊区'
        areaList = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/jinniu')
def jinniu():
    if session.get('user_name'):
        area = '金牛区'
        areaList = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/chenghua')
def chenghua():
    if session.get('user_name'):
        area = '成华区'
        areaList = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/longquanyi')
def longquanyi():
    if session.get('user_name'):
        area = '龙泉驿区'
        areaList = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/wenjiang')
def wenjiang():
    if session.get('user_name'):
        area = '温江区'
        areaList = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/xindu')
def xindu():
    if session.get('user_name'):
        area = '新都区'
        areaList = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/qinbaijiang')
def qinbaijiang():
    if session.get('user_name'):
        area = '青白江区'
        areaList = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/shuangliu')
def shuangliu():
    if session.get('user_name'):
        area = '双流区'
        areaList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))


@app.route('/HeatMap_chengdu/pidu')
def pidu():
    if session.get('user_name'):
        area = '郫都区'
        areaList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        areaEn = ['wuhou', 'jinjiang', 'qinyang', 'jinniu', 'chenghua', 'longquanyi', 'wenjiang', 'xindu',
                  'qinbaijiang',
                  'shuangliu', 'pidu']
        areaCh = ['武侯区', '锦江区', '青羊区', '金牛区', '成华区', '龙泉驿区', '温江区', '新都区', '青白江区', '双流区', '郫都区']
        return render_template("area.html",
                               username=session.get('user_name'),
                               area=area,
                               areaList=areaList,
                               areaEn=areaEn,
                               areaCh=areaCh)
    else:
        flash('You have not logged in,please log in first!')
        return redirect(url_for('login'))

@app.route('/app/login',methods=['GET','POST'])
def app_login():
    # a = request.args.get('xxx')
    # b = request.form['xxx']

    return jsonify({
        "isTrue":True
    })

if __name__ == '__main__':
    app.run()
