from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    email = db.Column(db.String(255))
    location= db.Column(db.String(80))
    biography= db.Column(db.String(500))
    created_on= db.Column(db.String(12))
    photo= db.Column(db.String(80))


    def __init__(self, fname, lname, gender,email,location,biography, created_on,photo ):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.gender= gender
        self.location= location
        self.biography= biography
        self.created_on= created_on
        self.photo= photo
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return "User: {0} {1}".format(self.fname, self.lname)
