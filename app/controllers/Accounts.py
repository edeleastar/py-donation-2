from flask import render_template, session, request, redirect
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from . import accounts
from app.models.User import User


class LoginForm(Form):
  email    = StringField('Email',    validators=[DataRequired()])
  password = StringField('Password', validators=[DataRequired()])

class SignupForm(Form):
  firstname = StringField('First Name', validators=[DataRequired()])
  lastname  = StringField('last Name',  validators=[DataRequired()])
  email     = StringField('Email',      validators=[DataRequired()])
  password  = StringField('Password',   validators=[DataRequired()])

@accounts.route('/')
def index():
  return render_template('accounts/index.html')

@accounts.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.objects(email=form.email.data).first()
    if user != None:
      if user.email == form.password.data:
        session['logged_in'] = True
        return redirect('/donation')
  return render_template('accounts/login.html', form=form)

@accounts.route('/signup', methods=['GET', 'POST'])
def logout():
  form = SignupForm()
  if form.validate_on_submit():
    user = User()
    form.populate_obj(user)
    user.ID=User.objects.count() + 1
    user.save()
    return redirect('/login')
  return render_template('accounts/signup.html', form=form)

@accounts.route('/logout')
def signup():
  session['logged_in'] = None
  return render_template('accounts/index.html')
