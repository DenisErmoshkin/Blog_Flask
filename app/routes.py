# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'DENIS'}
    return render_template('index.html', title='Home', user=user)

@app.route('/news')
def news ():
    return render_template('news.html')

@app.route('/blog')
def blog ():
    return render_template('blog.html')

@app.route('/shop')
def shop ():
    return render_template('shop.html')

@app.route('/about')
def about ():
    return render_template('about.html')