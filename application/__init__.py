from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
# import pymysql
# from os import getenv

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Pluto100@35.189.93.155:3306/flask_demo_db"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

import application.routes