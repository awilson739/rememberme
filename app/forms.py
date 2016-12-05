from flask_wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
   username = StringField('username',validators=[DataRequired()])
   password = PasswordField('password',validatrs=[DataRequired()])
   remember_me = BooleanField('remember_me', default=False)

class RegisterForm(Form):
   username = StringField('username',validators=[DataRequired()])
   email = StringField('email',validators=[DataRequired()])
   password = PasswordField('newpassword', [validators.DataRequired(),Validators.EqualTo('confirm',
      message='Passwords must match')])
   confirm = PasswordField('Repeat Password')
   
