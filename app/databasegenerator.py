import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Create table for multiple-choice questions
cursor.execute("CREATE TABLE multichoice (question TEXT, correctanswer TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT)")

# Create table for short-answer questions
cursor.execute("CREATE TABLE shortanswerquestions (question TEXT)")

# Create table for user
cursor.execute("CREATE TABLE user (username TEXT, email TEXT, password TEXT)")

multi_choice_list = [
    ("What is the capital of Australia?", "Melbourne", "Sydney", "Canberra", "Tokyo"),
    ("What is the capital of Germany?", "Berlin", "Munich", "Hamburg", "Paris"),
    ("Which planet is known as the Red Planet?", "Mars", "Jupiter", "Venus", "Earth"),
    ("What is the chemical symbol for water?", "H2O", "CO2", "O2", "H2SO4"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"),
    ("What is the tallest mammal on Earth?", "Giraffe", "Elephant", "Horse", "Lion"),
    ("What is the largest ocean on Earth?", "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"),
    ("Which country is known as the Land of the Rising Sun?", "Japan", "China", "South Korea", "Vietnam"),
    ("What is the square root of 64?", "8", "6", "10", "12"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo")
]

srt_answer_question_list = [
    ("What is the meaning of life?"),
    ("Who is the current President of the United States?"),
    ("What is the capital of France?"),
    ("What is the largest ocean on Earth?"),
    ("Who painted the Mona Lisa?")
]

user_list = [
        ("student", "test123@email.com", "test"),
]

# Insert multiple-choice questions
cursor.executemany("INSERT INTO multichoice VALUES (?, ?, ?, ?, ?)", multi_choice_list)

# Insert short-answer questions
cursor.executemany("INSERT INTO shortanswerquestions (question) VALUES (?)", [(question,) for question in srt_answer_question_list])

cursor.executemany("INSERT INTO user VALUES (?, ?, ?)", user_list)


connection.commit()
connection.close() 