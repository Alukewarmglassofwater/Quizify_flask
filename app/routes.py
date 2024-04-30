from app import app
from flask import render_template

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
    return render_template('login.html', title='Sign In')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')


@app.route('/quizmcq')
def quizmcq():
    return render_template('quizmcq.html', title='Multichoice')


@app.route('/quizsa')
def quizsa():
    return render_template('quizsa.html', title='Shortanswer')