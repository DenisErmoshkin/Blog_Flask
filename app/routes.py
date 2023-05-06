# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login ():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}' .format(form.username.data, form.remember_me.data))
        return redirect('/index')
        #...#
    return render_template('login.html', form=form)



