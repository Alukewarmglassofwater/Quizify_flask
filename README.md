# app folder
- Main stuff
- templates: html file
- static: css and images files

# requirements.txt
- install flask and extra module using this
## For installation of flask module
1. `venv\Scripts\activate.bat` activate venv for Windows
2. `pip install -r requirements.txt` - python will install everything listed in txt file

## For update flask module for team to see
1. `venv\Scripts\activate.bat` activate venv for Windows
2. `pip freeze > requirements.txt` - module list will be exported to txt file
3. `git push origin`

# Miscellaneous
- .flaskenv : 
    1. `venv\Scripts\activate.bat` activate venv for Windows
    2. `pip install python-dotenv`
    3. no need to have extra step of 'FLASK_APP=quizify.py' just `flask run`

- .gitignore
    1. ignore venv file

- Username: test@gmail.com
- Pass: test

