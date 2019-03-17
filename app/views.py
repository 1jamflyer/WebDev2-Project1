import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import UserProfile
from werkzeug.utils import secure_filename
from app.models import User
import psycopg2
import datetime 
from sqlalchemy import exc

#conn = psycopg2.connect("host=localhost dbname=UserProfiles user=project1")




 

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile',methods=["GET", "POST"])
def profile(): 
    """Add a new profile"""
    form = UserProfile()
    def new_profile():
        form = UserProfile()

        if request.method == "POST" and form.validate_on_submit():
            firstname = UserProfile.fname.data
            lastname = UserProfile.lname.data
            gender = UserProfile.gender.data
            email = UserProfile.email.data
            location = UserProfile.location.data
            biography = UserProfile.biography.data
            created_on = str(datetime.datetime.now()).split()[0]
                
            photo = UserProfile.photo.data
            photo_name = secure_filename(photo.filename)
                
            user = User(firstname, lastname, gender, email, location, biography, created_on, photo_name)
                
            db.session.add(user)
            db.session.commit()
                
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photo_name))
                
            flash("Profile Added", "success")
            return redirect(url_for("profiles"))
        else:
            flash("Error occured")
            return render_template('profile.html', form=form)
    return render_template('profile.html', form=form)

@app.route("/profiles")
def profiles():
    users = User.query.all()
    profiles = []
    
    for user in User:
        profiles.append({"pro_pic": user.photo, "f_name":user.firstname, "l_name": user.lastname, "gender": user.gender, "location":user.location, "id":user.id})
    
    return render_template("profile_lost.html", profiles = profiles)

@app.route('/profile/<userid>')
def i_profile(userid):
    user = User.query.filter_by(id=userid).first()
    
    if user is None:
        return redirect(url_for('home'))
        
    c_y = int(user.created_on.split("-")[0])
    c_m = int(user.created_on.split("-")[1])
    c_d = int(user.created_on.split("-")[2])
    
    user.created_on = format_date_joined(c_y, c_m, c_d)
    
    return render_template("v_profile.html", user=user)

def format_date_joined(yy,mm,dd):
    return datetime.date(yy,mm,dd).strftime("%B, %d,%Y")


def read_file(filename):
    data = ""
    
    with open(filename, "r") as stream:
        data = stream.read()
        
    return data
 

    
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
