from flask import render_template, flash, redirect
from .forms import LoginForm
from app import app
@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html',title="Remember Me!")

@app.route('/login',methods=['GET','POST'])
def login():
   form = LoginForm()
   return render_template('login.html',title='Sign In',form=form)
