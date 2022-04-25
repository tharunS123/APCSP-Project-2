# Modules that are given by the Python Flask, SQLAlchemy. 
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# This class method from flask will create tables in the database.db file.  
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  date = db.Column(db.DateTime(timezone=True),default=func.now()) # time that user was added. 
