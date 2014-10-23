from flask import render_template, session, request, redirect
from . import accounts
from app.models.User import User

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
  user = User (firstname=request.form['firstName'], lastname=request.form['lastName'],
               email=request.form['email'], password  = request.form['password'],
               ID=User.objects.count() + 1)
  user.save()
  return redirect('/')

@accounts.route('/authenticate', methods=['POST'])
def authenticate():
  matches = User.objects(email=request.form['email'])
  if matches.count() > 0:
    user = matches.get(0)
    if user.email == request.form['password']:
      session['logged_in'] = True
      return redirect('/donation')
  return redirect('/')