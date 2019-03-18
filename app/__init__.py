from flask import Flask
from subprocess import call
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zyzkngoszxvajy:31e15b4bc549faa6778e150e767eb0fc0ffa0a4cc37c012a0cf88303b0486c07@ec2-184-73-216-48.compute-1.amazonaws.com:5432/db7g7fcbnkitgr"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

allowed_exts = ["jpg", "jpeg", "png"]
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views

#postgresql://project1:jonno@localhost/userprofiles