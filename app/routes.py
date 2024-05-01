from app import app
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/favicon', 'favicon.ico', mimetype='image/x-icon')

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Login is required.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    ##handles login. email= test@gmail.com | Password= test
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
@login_required
def logout():
    session.pop('logged_in', None)
    flash('Logout successful!')
    return redirect('/login')

@app.route('/home')
@login_required

def home():
    user = {'username': 'Teststudent'}
    return render_template('home.html', title='Home')


@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/quizmcq')
def quizmcq():
    return render_template('quizmcq.html', title='Multichoice')


@app.route('/quizsa')
def quizsa():
    return render_template('quizsa.html', title='Shortanswer')
