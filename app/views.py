from flask import render_template, flash, redirect, sessions, url_for, request,g
from flask_login import login_user, logout_user, current_user, login_required 
from .forms import LoginForm
from app import app,db,lm
from .models import User 
@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html',title="Remember Me!")

@app.route('/login',methods=['GET','POST'])
def login():
   if g.user is not None and g.user.is_authenticated:
      return redirect(url_for('index'))
   form = LoginForm()
   if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      return True ###Add log in stuff
      flash('Login requested for','remember_me=%s'% str(form.remember_me.data))
      return redirect('/index')
   return render_template('login.html',title='Sign In',form=form)

@lm.user_loader
def load_user(id):
   return User.query.get(int(id))
###After login response
@app.route('/register')
def register():
   return True 

@app.before_request
def before_request():
   g.user = current_user

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('index')) 
