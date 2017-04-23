from flask_wtf import Form
from wtforms import StringField, PasswordField,validators
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    email = EmailField('Email address', validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Give the password', validators=[DataRequired()])


class Otp(Form):
    key = StringField('username', validators=[DataRequired()])