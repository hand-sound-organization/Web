import os
from datetime import timedelta
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SECRET_KEY = os.urandom(24)
PERMANENT_SESSION_LIFETIME = 1800 # timedelta(days=7)