# Install Guide

Due to the application being based on Flask everything is contained inside the Quizify_flask folder. Extra python modules that the application uses are listed and installed via the requirements.txt file. 

## Windows

## Miscellaneous
- .flaskenv : 
    1. `venv\Scripts\activate.bat` activate venv for Windows
    2. `pip install python-dotenv`
    3. no need to have extra step of 'FLASK_APP=quizify.py' just `flask run`


## macOS

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

## Linux

1. Install Git
- Below command is for Debian. If running another distribution install package from specific package manager
`$sudo apt install git`

2. Git clone the repository
- this will clone the Quizify_flask project into your current directory
- advised to mkdir a 'tmp' directory and cd into that
`$mkdir tmp`
`$cd tmp`
`/tmp $`
`$git clone https://github.com/Alukewarmglassofwater/Quizify_flask`

3. Python environment setup
- Install python package onto your system
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

## Windows

1. Git clone the repository: 
- Git clone https://github.com/Alukewarmglassofwater/Quizify_flask 
- This will download the contents of quizify_flask into your current terminal directory. 

2. Inside the app folder, activate the virtual environment. 
- python3 -m venv venv 
  - This creates a folder called ‘venv’ which contains the virtual python3 install and any required packages. 
- Activate venv 
  - Cd into directory where venv file is present. 
  - venv\Scripts\activate.bat (Windows) 
   - Terminal should update with (venv). This indicates the venv has been activated. 

3. Download module required for the project. 
- Requirements.txt is a text file that contains all the dependencies used for the project. 
- Install packages contained in requirement.txt into your venv file. 
  - pip install -r requirements.txt. 

4. Run the program and make sure you’re still in the venv. 
- The program runs from a file called ‘quizify.py’ 
- Make sure you are in this directory before running the next command. 
- Set FLASK_RUN variable: 
  - set FLASK_RUN=quizify.py (optional) 
  - This tells flask that when the flask run command is invoked, initialise from the quizify.py file. 
- flask run 
  - This should load a prompt that states "Running on http://127.0.0.1:5000"
  - This URL can be loaded into a browser to view the flask project. 

