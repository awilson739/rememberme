
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from config import basedir 
lm = LoginManager()
lm.init_app(app)
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views,models
