from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Beautiful day in Portland!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)