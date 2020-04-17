from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(20))

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    db.create_all()