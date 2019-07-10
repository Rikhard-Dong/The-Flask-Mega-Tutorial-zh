from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegisterForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user, login_required
from werkzeug.urls import url_parse


@app.route("/")
@app.route('/index')
@login_required
def index():
    user = {"username": "ride"}
    posts = [
        {
            'author': {'username': '鲁迅'},
            'body': '中国最伟大的艺术就是男人扮女人'
        },
        {
            'author': {'username': '林则徐'},
            'body': '苟利国家生死以, 岂因祸福避趋之!'
        }
    ]
    return render_template("index.html", title="home", posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash("无效的用户名或者密码")
            return redirect(url_for("login"))
        login_user(user, remember=remember_me)
        # 下一页
        next_page = request.args.get('next')
        if next_page is None or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='登陆', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("恭喜! 注册成功!")
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)
