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
   if form.validate_on_submit():
      flash('Login requested for','remember_me=%s'% str(form.remember_me.data))
      return redirect('/index')
   return render_template('login.html',title='Sign In',form=form)
