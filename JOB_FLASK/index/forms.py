from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField
from index.models import User

class RegistrationForm(FlaskForm):
    firstname        = StringField('First Name', validators=[DataRequired()]) # DataRequired means it cant be empty
    lastname         = StringField('Last Name', validators=[DataRequired()])
    college          = StringField('College', validators=[DataRequired()])
    email            = EmailField('Email', validators=[DataRequired(), Email()])
    password         = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit           = SubmitField('Sign Up')
    def validate_firstname(self, firstname):
        user = User.query.filter_by(firstname = firstname.data).first()
        if user:
            raise ValidationError('User Already Exists!')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email Already Exists!')

class LoginForm(FlaskForm):
    email    = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit   = SubmitField('Login')