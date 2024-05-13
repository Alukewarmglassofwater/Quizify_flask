####Install Guide####

Due to the application being based on Flask everything is contained inside the Quizify_flask folder. Extra python modules that the application uses are listed and installed via the requirements.txt file. 

##########################Windows########################

# Miscellaneous
- .flaskenv : 
    1. `venv\Scripts\activate.bat` activate venv for Windows
    2. `pip install python-dotenv`
    3. no need to have extra step of 'FLASK_APP=quizify.py' just `flask run`


##########################macOS########################

1. Homebrew package manager install
`$/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

2. Install Git
 `$ brew install git`

3. Git clone the repository
- this will clone the Quizify_flask project into your current directory
- advised to mkdir a 'tmp' directory and cd into that
`$mkdir tmp`
`$cd tmp`
`/tmp $`
`$git clone https://github.com/Alukewarmglassofwater/Quizify_flask`

- The file structure should look like this at this point:
```bash
.
└── tmp/
    └── Quizify_flask/
        ├── requirements.txt 
        ├── quizify.py 
        ├── README.md
        ├── .gitignore
        ├── .flaskenv
        ├── __pycache__
        ├── app
        ├── instance
        ├── static
        └── templates
```
- cd into Quizify_flask
`$cd Quizify_flask`
- Install pip, the python package manager
`$pip install virtualenv`
- Create virtual environment
`$python3 -m venv venv`
- File structure should now look like this
```bash
.
└── tmp/
    └── Quizify_flask/
        ├── requirements.txt 
        ├── quizify.py 
        ├── README.md
        ├── .gitignore
        ├── .flaskenv
        ├── __pycache__
        ├── app
        ├── instance
        ├── static
        ├── templates
        └── venv (### venv folder created ###)
```
- Activate virtual environment
`$source venv/bin/activate`
- Prompt should change to reflect the virtual environment
`(venv) $`
- Virtual environment now set up
 
5. Flask modules install
`$pip install -r requirements.txt`

6. Flask setup and configuration
- Point flask run variable to the quizify.py file
`$export FLASK_RUN=quizify.py`

7. Run flask application
`$flask run`

8. View flask application
- Navigate to provided URL in your browser: 
`http://127.0.0.1:5000`

##########################Linux########################

1. Install Git
- Below command for Debian. If running another distribution install git package from specific package manager
`$sudo apt install git`

2. Git clone the repository
- this will clone the Quizify_flask project into your current directory
- advised to mkdir a 'tmp' directory and cd into that
`$mkdir tmp`
`$cd tmp`
`/tmp $`
`$git clone https://github.com/Alukewarmglassofwater/Quizify_flask`

3. Python environment setup
###install python package onto your system
Download installer and run from https://www.python.org/downloads/macos/

##Linux
Open a terminal and, depending on the package manager, install the python3 package. A Debian example is given below.
- Debian install
`$sudo apt install python3`
- Verify install
Verify install by opening a terminal and run below. An output should be generated. 
`$python --version`
- OR
Open "Python IDLE" application on your system.

4. Python virtual environment setup

- The file structure should look like this at this point:
```bash
.
└── tmp/
    └── Quizify_flask/
        ├── requirements.txt 
        ├── quizify.py 
        ├── README.md
        ├── .gitignore
        ├── .flaskenv
        ├── __pycache__
        ├── app
        ├── instance
        ├── static
        └── templates
```
- cd into Quizify_flask
`$cd Quizify_flask`
- Install pip, the python package manager
`$pip install virtualenv`
- Create virtual environment
`$python3 -m venv venv`
- File structure should now look like this
```bash
.
└── tmp/
    └── Quizify_flask/
        ├── requirements.txt 
        ├── quizify.py 
        ├── README.md
        ├── .gitignore
        ├── .flaskenv
        ├── __pycache__
        ├── app
        ├── instance
        ├── static
        ├── templates
        └── venv (### venv folder created ###)
```
- Activate virtual environment
`$source venv/bin/activate`
- Prompt should change to reflect the virtual environment
`(venv) $`
- Virtual environment now set up

5. Flask modules install
`$pip install -r requirements.txt`

6. Flask setup and configuration
- Point flask run variable to the quizify.py file
`$export FLASK_RUN=quizify.py`

7. Run flask application
`$flask run`

8. View flask application
- Navigate to provided URL in your browser: 
http://127.0.0.1:5000


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

