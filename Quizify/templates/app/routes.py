from flask import render_template, url_for
from app import app
from app.forms import LoginForm
from flask import send_from_directory

import os

#don't know why this is broken
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/favicon', 'favicon.ico', mimetype='image/x-icon')


@app.route('/')
@app.route('/home')

def home():
    user = {'username': 'Teststudent'}
    return render_template('home.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()  # Create an instance of the LoginForm class
    if form.validate_on_submit():
        # Add your login logic here
        return redirect(url_for('home'))  # Redirect to home page after successful login
    return render_template('login.html', title='Login', form=form)

@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/quizmcq')
def quizmcq():
    return render_template('quizmcq.html', title='Multichoice')


@app.route('/quizsa')
def quizsa():
    return render_template('quizsa.html', title='Shortanswer')
