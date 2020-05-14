from app import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(20))
    time = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.username


class DistrictInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.String)
    time = db.Column(db.DateTime)

    def __repr__(self):
        return '<DistrictInfo %r>' % self.name

class CityHeatMap(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    lng = db.Column(db.Float,nullable=False)
    lat = db.Column(db.Float,nullable=False)
    count = db.Column(db.Integer,nullable=False)
    time = db.Column(db.DateTime)

    def __repr__(self):
        return '<CityHeatMap (%r,%r)>' % (self.lng,self.lat)


class AttackLog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    lock_id = db.Column(db.Integer,nullable=False)
    attack_time  = db.Column(db.DateTime)
    lng = db.Column(db.Float)
    lat = db.Column(db.Float)
    isSafe = db.Column(db.BOOLEAN)

    def __repr__(self):
        return '<AttackLog (%r,%r)>' % (self.lng,self.lat)


class WarningInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String)
    name = db.Column(db.String)
    occur_time = db.Column(db.String)
    username = db.Column(db.String(50))

    def __repr__(self):
        return '<WarningInfo>'


class APPUser(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    lock_id = db.Column(db.Integer)
    lng = db.Column(db.Float)
    lat = db.Column(db.Float)
    memberlist = db.Column(db.String,default='')
    safeday = db.Column(db.Integer,default=0)
    safetimes = db.Column(db.Integer,default=0)
    member = db.Column(db.Integer,default=0)
    safepct = db.Column(db.String,default='100%')
    timestart = db.Column(db.String,default='')
    timeend = db.Column(db.String,default='')
    datalist = db.Column(db.String,default='')





    def __repr__(self):
        return '<APPUser>'


