from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import os
import sqlite3



app = Flask(__name__)
app.secret_key = "secrets"


from app import routes