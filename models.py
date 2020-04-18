from app import db


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




