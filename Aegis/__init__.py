from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#initialize the flask app
app = Flask(__name__)

#tell sqlalchemy where the database file is
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#initialize the database
db = SQLAlchemy(app)

from Aegis import routes