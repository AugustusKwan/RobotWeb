from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Keep me Logged in')
    Submit = SubmitField('登錄')

class RegisterForm(FlaskForm):
    phone = StringField('Phone',validators=[DataRequired(),Length(1,11)])
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    password1 = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password',message = '密碼必須要一致')])
    Submit = SubmitField('注冊')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password',validators=[DataRequired()])
    new_password = PasswordField('New Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password',validators=[DataRequired(),EqualTo('New Password',message='密碼必須要一致')])
    Submit = SubmitField('更改密碼')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password',validators=[DataRequired()])
    new_password = PasswordField('New Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password',validators=[DataRequired(),EqualTo('New Password',message='密碼必須要一致')])
    Submit = SubmitField('更改密碼')

class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Length(1, 64),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

