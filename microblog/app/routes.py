from app import app
from flask import render_template


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
