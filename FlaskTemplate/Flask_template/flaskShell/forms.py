from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskShell.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username): 
        user = User.query.filter_by(username=username.data).first()
        if user: 
            raise ValidationError("Username has been taken. Please choose a different one.")

    def validate_email(self, email): 
        email = User.query.filter_by(email=email.data).first()
        if email: 
            raise ValidationError("Email has been used. Please choose a different one.")

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class JournalForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = StringField('Share your Thoughts',validators=[DataRequired()])
    entry_date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = StringField('Add')


class UpdateForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField('Update')

    def validate_username(self, username): 
        if username.data != current_user.username: 
            user = User.query.filter_by(username=username.data).first()
            if user: 
                raise ValidationError("Username has been taken. Please choose a different one.")

    def validate_email(self, email): 
        if email.data != current_user.email: 
            email = User.query.filter_by(email=email.data).first()
            if email: 
                raise ValidationError("Email has been used. Please choose a different one.")