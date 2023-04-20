# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'DENIS'}
    return render_template('index.html', title='Home', user=user)

@app.route('/blog')
def blog ():
    return "HELLO THIS IS MY BLOG, NICE TO MEET U <br> and HAVE A GOOD DAY, BITCHES!"

@app.route('/about')
def about ():
    return "HELLO THIS IS SECTION ABOUT, NICE TO MEET U <br> and HAVE A GOOD DAY, BITCHES!"