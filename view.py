from app import app, db
from flask import render_template, request, jsonify
from models import User
import json
import base64

@app.route('/')
def login():
    return render_template("login.html")


@app.route('/HeatMap_chengdu')
def register():
    return render_template("start1.html")



if __name__ == '__main__':
    app.run()
