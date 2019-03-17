from flask import Flask
from subprocess import call
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:jonno@localhost/userprofiles"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

allowed_exts = ["jpg", "jpeg", "png"]
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
