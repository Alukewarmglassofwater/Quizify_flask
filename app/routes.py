from app import app
from flask import Flask, render_template, redirect, url_for, request, session, flash

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/favicon', 'favicon.ico', mimetype='image/x-icon')


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'test@gmail.com' or request.form['password'] != 'test':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('Login successful!')
            return redirect(url_for('home'))
    return render_template('/login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout successful!')
    return redirect('/login')

@app.route('/home')

def home():
    user = {'username': 'Teststudent'}
    return render_template('home.html', title='Home', user=user)


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/quizmcq')
def quizmcq():
    return render_template('quizmcq.html', title='Multichoice')


@app.route('/quizsa')
def quizsa():
    return render_template('quizsa.html', title='Shortanswer')