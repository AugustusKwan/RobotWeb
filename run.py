from flask import Flask,render_template,flash,redirect,url_for,session
from threading import Thread
#import click
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from app.auth.form import LoginForm,RegisterForm,ChangePasswordForm,ChangeEmailForm
from flask_sqlalchemy import SQLAlchemy
#from flask_script import Manager
from app.models import User,Role
from app.ext import db
from flask_migrate import Migrate
from flask_mail import Mail,Message

import os 
import json

with open('E:\\Robot\\JSON\PW.JSON','r') as json_f:
    json_dict = json.load(json_f)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:"+ json_dict['DB_PASSWORD'] +"@localhost:3306/robot"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = json_dict['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = json_dict['MAIL_PASSWORD']
app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[FLASKY]'
app.config['FLASK_MAIL_SENDER'] = 'Flasky Admin <williamkwan@126.com>'


bootstrap = Bootstrap(app)
moment = Moment(app)
db.init_app(app)
migrate = Migrate(app,db)
mail = Mail(app)
#manager = Manager(app)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to,subject,template,**kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX']+subject,sender=app.config['FLASK_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


@app.route('/')
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
    return render_template('index.html',username=name)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.email.data).first()
        if user is None:
            user = User(username = form.email.data)
            db.session.add(user)
            session['know'] = False
        else:
            session['know'] = True
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
         flash('你已經成功登錄') 
    return render_template('register.html',form=form)

@app.route('/change-password',methods=['GET','POST'])
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        flash('你已成功修改密碼！')
        return redirect(url_for('auth/change_password.html'))
    return render_template('auth/change_password.html',form=form)

@app.route('/change-email',methods=['GET','POST'])
def change_email() :
    form = ChangeEmailForm()
    if form.validate_on_submit():
        flash('已成功修改郵箱！')
    return render_template('auth/change_email.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
