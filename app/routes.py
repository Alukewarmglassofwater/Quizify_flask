from app import app
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, send_from_directory
from functools import wraps
import sqlite3
import re

# Connect to .db file
DATABASE = 'app/instance/database.db'

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


@app.route('/register', methods = ['GET', 'POST'])
def register():
    mesage = ''
    # Check if user fill the form or not or is it the correct format
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM user WHERE email = ?', (email,))
        account = c.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            c.execute('''INSERT INTO user (name, email, password)VALUES (?, ?, ?)''', 
                      (userName, email, password))
            conn.commit()
            conn.close() 
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

#possibly mcq quiz logic?? not really sure how it works??
# Fetch questions and answers from the database
def get_question(index):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM multichoice LIMIT 1 OFFSET ?", (index,))
    question_data = cursor.fetchone()
    conn.close()
    return question_data

@app.route('/quizmcq', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Get selected answer
        selected_answer = request.form['answer']
        # Check the selected answer and do something (e.g., store results)
        # For simplicity, let's just print the selected answer for now
        print("Selected Answer:", selected_answer)

        # Increment the question index for the next question
        index = int(request.args.get('index', 0)) + 1
        return redirect(url_for('quiz', index=index))

    # Get the current question index from query parameter
    index = int(request.args.get('index', 0))

    # Fetch the question and answer options from the database
    question_data = get_question(index)
    if question_data:
        question, answer1, answer2, answer3, answer4 = question_data
        options = [answer1, answer2, answer3, answer4]
        return render_template('quizmcq.html', question=question, options=options, index=index)
    else:
        # No more questions, quiz completed
        return "Quiz completed!"

@app.route('/quizsa', methods=['GET', 'POST'])
def quizsa():
    if request.method == 'POST':
        # Get the submitted question index
        question_index = int(request.form['index'])

        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Fetch short-answer questions from the database
        cursor.execute("SELECT question FROM shortanswerquestions")
        questions = [row[0] for row in cursor.fetchall()]

        # Check if the index is valid
        if 0 <= question_index < len(questions):
            # Increment the question index for the next question
            next_index = question_index + 1

            # Check if there are more questions
            if next_index < len(questions):
                # Fetch the next question
                next_question = questions[next_index]
                conn.close()
                return render_template('quizsa.html', title='Shortanswer', question=next_question, index=next_index)

        # No more questions, quiz completed
        conn.close()
        return "Quiz completed!"

    else:
        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Fetch the first short-answer question from the database
        cursor.execute("SELECT question FROM shortanswerquestions LIMIT 1")
        first_question = cursor.fetchone()[0]

        # Close the database connection
        conn.close()

        return render_template('quizsa.html', title='Shortanswer', question=first_question, index=0)
