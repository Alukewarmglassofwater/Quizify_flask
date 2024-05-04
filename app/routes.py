from app import app
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, send_from_directory
from functools import wraps
import sqlite3



DATABASE = 'app/database.db'

# Fetch questions and answers from the database
def get_question(index):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM multichoice LIMIT 1 OFFSET ?", (index,))
    question_data = cursor.fetchone()
    conn.close()
    return question_data

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
    """  
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
    """

    return render_template('register.html', title='Register')

#possibly mcq quiz logic?? not really sure how it works??
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
