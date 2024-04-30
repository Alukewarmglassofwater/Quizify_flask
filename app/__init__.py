from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin



app = Flask(__name__)

from app import routes