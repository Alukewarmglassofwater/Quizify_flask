from app import app
from flask import render_template, request
import sqlite3

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
    if request.method == "POST":
       username = request.form.get("username")
       password = request.form.get("password")
    return render_template('login.html', title='Sign In')

@app.route('/register', methods=['GET', 'POST'])
def register():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    username = request.form.get("username")
    password = request.form.get("password")

    # Connect to SQLite database and insert data
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (first_name TEXT, last_name TEXT, username TEXT, password TEXT)''')
    c.execute('INSERT INTO users (first_name, last_name, username, password) VALUES (?, ?, ?, ?)',
              (first_name, last_name, username, password))
    conn.commit()
    conn.close()

    return render_template('register.html', title='Register')


@app.route('/quizmcq')
def quizmcq():
    return render_template('quizmcq.html', title='Multichoice')


@app.route('/quizsa')
def quizsa():
    return render_template('quizsa.html', title='Shortanswer')