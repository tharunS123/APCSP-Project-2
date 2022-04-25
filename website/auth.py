# Modules that are given by the Python Flask. 
from flask import Blueprint,render_template,request,flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__) # Url prefix blueprint used in __init__.py file

# Login page function 
@auth.route('/login', methods=['GET','POST']) # html page routes that display in website.
def login():
  # Checking if the user as logged in before
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password,password):
        flash('Logged in Successfully!', category='success')
        login_user(user,remember=True)
        return redirect(url_for('views.home'))
      else:
        flash('Incorrect password, try again.', category='error')
    # If the user is not signed in before, this error message will be display. 
    else: 
      flash('Email does not exist. ',category='error')

  return render_template('login.html',user=current_user)

# Logout Page function
@auth.route('/logout')
@login_required # methods to condition if the user logged in, then display the logout button in Navbar.
def logout():
  logout_user()
  return redirect(url_for('auth.login')) # redirect to login page.

# Sign up function
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
  # This If statement will check to see the sign.html page as given the Input
  if request.method == 'POST':
    # This block of code will add the input in the sign up page to the database. 
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    # Conditions for making a stonrg password and email enter by the user. 
    user = User.query.filter_by(email=email).first()
    if user:
      flash('Email already exists. ',category='error')
    elif len(email) <4:
      flash('Email must be greater than 3 characters.', category='error')
    elif len(first_name) < 2:
      flash('First name must be greater than 1 character.', category='error')
    elif password1 != password2:
      flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
      flash('Password must be at least 7 characters.', category='error')
    # This else statement will redirects to the login page after adding it to the database. 
    else:
      new_user = User(email=email, first_name=first_name, password=generate_password_hash(
        password1, method='sha256'))
      db.session.add(new_user)
      db.session.commit()
      flash('Accout created!',category='success')
      return redirect(url_for('views.home'))


  return render_template('sign-up.html',user=current_user) # This will open sign-up.html page. 