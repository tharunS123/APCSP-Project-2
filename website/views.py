# Modules that are given by the Python Flask. 
from flask import Blueprint,render_template
from flask_login import login_required, logout_user, current_user

views = Blueprint('views',__name__) # Url prefix blueprint used in __init__.py file

# This block will return the home.html after the user have signed in. 
@views.route('/')
@login_required
def home():
  return render_template('home.html',user=current_user)