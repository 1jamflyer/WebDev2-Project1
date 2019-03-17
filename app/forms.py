from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, Email


class UserProfile(FlaskForm):
    fname = StringField('First name', validators=[InputRequired()])
    lname = StringField('Last name', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('Male'), ('Female')])
    email = StringField("email",validators=[InputRequired(), Email()])
    location= StringField('location', validators=[InputRequired()])
    biography= TextAreaField('biography', validators=[InputRequired()])
    photo = FileField('image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    