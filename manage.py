from flask import Flask,render_template,flash,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from app.auth.form import LoginForm,RegisterForm,ChangePasswordForm,ChangeEmailForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    flash('This is the new page')
    return '<h1>Hello World!</h1>'

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         flash('你已經成功登錄') 
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
