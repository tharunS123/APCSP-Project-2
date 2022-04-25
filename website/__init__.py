# Modules that are given by the Python Flask. 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LOGIN_MESSAGE, LoginManager

db = SQLAlchemy() # Assigning SQLAlchemy modules to a variable called db. 
DB_NAME = "database.db" # The name of Database file

# This function will be called in main.py file.
# This def will create the website from the Blueprint in each py file used in this program. 
def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '1234567' # Create a secret key to make the code encrypted. 
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Configuring the Database file. 
  db.init_app(app)

  from .views import views
  from .auth import auth
  from .models import User

  # Making a url prefix for each python file redirect html file. 
  app.register_blueprint(views,url_prefix='/')
  app.register_blueprint(auth,url_prefix='/auth/')

  create_database(app) # Calling the creating db function to add it to the program.

  # Logic for user access. 
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))
  
  return app

# This function will create the database inside this program folder. 
def create_database(app):
  if not path.exists('website/' + DB_NAME):
    db.create_all(app=app)
    print('Created Database!')