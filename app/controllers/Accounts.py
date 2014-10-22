from flask import render_template, session, request, redirect
from . import accounts
from app.models.User import User
from app.models.User import users


@accounts.route('/')
def index():
  return render_template('accounts/index.html')

@accounts.route('/login')
def login():
  return render_template('accounts/login.html')

@accounts.route('/signup')
def logout():
  return render_template('accounts/signup.html')

@accounts.route('/logout')
def signup():
  return render_template('accounts/index.html')

@accounts.route('/register', methods=['POST'])
def register():
  firstname = request.form['firstName']
  lastname  = request.form['lastName']
  email     = request.form['email']
  password  = request.form['password']
  users[email] = (User (firstname, lastname, email, password))
  return redirect('/')

@accounts.route('/authenticate', methods=['POST'])
def authenticate():
  email     = request.form['email']
  password  = request.form['password']
  if email in users and password == users[email].password:
    session['logged_in'] = True
    return redirect('/donation')
  else:
    return redirect('/')