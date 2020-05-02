from app import app, db
from flask import render_template, request, jsonify, redirect, url_for, session, flash
from models import *
import random
import json
import base64
from datetime import datetime, time


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


@app.route('/HeatMap_chengdu/HeatPointMap/data', methods=['POST'])
def heatpoint_data():
    pointdist = {"point": []}
    points = CityHeatMap.query.all()
    for point in points:
        pointdist["point"].append(json.dumps({
            "position":[point.lng - 12.4, point.lat - 9.3]
        }))
    point_jsondata = json.dumps(pointdist)
    return jsonify(point_jsondata)


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


# @app.route('/app/getwarning',methods=['POST'])
# def app_login():
#     lock_id = request.form['lock_id']
#     time = request.form['time']
#
#     return jsonify({
#         "isTrue":True
#     })


@app.route('/app/WarningInfo',methods=['GET','POST'])
def app_WarningInfo():
    if request.method == 'GET':
        queryInfo = WarningInfo.query.all()
        column_list = []
        for item in queryInfo:
            column_dict = {}
            column_dict['name'] = item.name
            column_dict['event'] = item.event
            column_dict['occur_time'] = item.occur_time
            column_list.append(column_dict)
        return jsonify({"returnInfo": column_list})
    else:
        newWarning = WarningInfo(name=request.form['name'],
                                 event=request.form['event'],
                                 occur_time=datetime.strptime(request.form['occur_time'], "%Y-%m-%d %H:%M:%S"))
        db.session.add(newWarning)
        if request.form['event'] == '攻击':
            appuser = APPUser.query.filter(APPUser.username == request.form['app_username'],
                                           APPUser.lock_id == int(request.form['lock_id'])).first()
            newAttackLog = AttackLog(lock_id=int(request.form['lock_id']),
                                     attack_time=datetime.strptime(request.form['occur_time'], "%Y-%m-%d %H:%M:%S"),
                                     lng=round(appuser.lng, 2),
                                     lat=round(appuser.lat, 2),
                                     isSafe=request.form['isSafe'] == 'True')
            db.session.add(newAttackLog)
            newCityHeatMap = CityHeatMap(lng=appuser.lng,
                                         lat=appuser.lat,
                                         count=50,
                                         time=datetime.strptime(request.form['occur_time'], "%Y-%m-%d %H:%M:%S"))
            db.session.add(newCityHeatMap)
            db.session.commit()
            db.session.close()
        return "Message is sent Successfully !"


if __name__ == '__main__':
    # appuser = APPUser(username='lsd',lock_id=2020,lng=116.591031 - 12.4,lat=39.540089 - 9.3)
    # db.session.add(appuser)
    # db.session.commit()
    # a1 = WarningInfo.query.get(1)
    # db.session.delete(a1)
    # db.session.commit()
    # a1 = WarningInfo(name='用户1', event='开门', occur_time='2020-04-21 21:36')
    # a2 = WarningInfo(name='攻击者', event='攻击', occur_time='2020-04-22 03:06')
    # a3 = WarningInfo(name='用户1', event='开门', occur_time='2020-04-22 12:51')
    # a4 = WarningInfo(name='陌生人', event='试错', occur_time='2020-04-22 13:23')
    # a5 = WarningInfo(name='用户1', event='开门', occur_time='2020-04-22 18:16')
    # db.session.add(a5)
    # db.session.add(a4)
    # db.session.add(a3)
    # db.session.add(a2)
    # db.session.add(a1)
    # db.session.commit()
    app.run(host='0.0.0.0')
