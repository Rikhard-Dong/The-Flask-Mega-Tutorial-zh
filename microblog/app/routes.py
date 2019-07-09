from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route("/")
@app.route('/index')
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
    return render_template("index.html", title="home", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('登陆用户 {}, 记住我={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='登陆', form=form)
