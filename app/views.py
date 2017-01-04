from flask import render_template, flash, redirect, sessions, url_for, request,g
from flask_login import login_user, logout_user, current_user, login_required 
from .forms import LoginForm,RegisterForm
from app import app,db,lm
###add from app import lm
from .models import User 
@app.route('/')
@app.route('/index')
@login_required	
def index():
   user = g.user
   return render_template('index.html',title="Remember Me!",user=user)

@app.route('/login',methods=['GET','POST'])
def login():
   if g.user is not None and g.user.is_authenticated:
      return redirect(url_for('index'))
   form = LoginForm()
   user = User()
   if form.validate_on_submit():
      login_user(user)
      next = request.args.get('next')
      #session['remember_me'] = form.remember_me.data
      flash('Logged in')
      return redirect(next or url_for('index'))
   return render_template('login.html',title='Sign In',form=form)

@lm.user_loader
def load_user(id):
   if id is None or id == 'None':
      id = -1
   return User.query.get(int(id))
###After login response

@app.route('/register',methods=['GET','POST'])
def register():
   form = RegisterForm()
   if form.validate_on_submit():
      user = User(username=form.username.data, email=form.email.data,
                  password=form.password.data)
      db.session.add(user)
      db.session.commit()
      flash('Thanks for registering')
      return redirect(url_for('login'))
   return render_template('register.html',form=form,title='Register')

@app.before_request
def before_request():
   g.user = current_user

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('index')) 
