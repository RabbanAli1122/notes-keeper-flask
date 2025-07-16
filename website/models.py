from . import db #. means __init__
from flask_login import UserMixin #UserMixin is a class provided by Flask-Login to help manage user sessions. It provides default implementations of methods required by Flask-Login such as is_authenticated, is_active, is_anonymous, and get_id().
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)# this is the id of note 
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id= db.Column(db.Integer,db.ForeignKey("user.id"))
#^^above is the one to many realtionship where one user has many notes

class User(db.Model, UserMixin):#db.model creates the class' reltionship with the database and make it database controlable
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150)) 
    notes = db.relationship('Note') # it tells flask and SQLalchemy that everytime a user creates a note, add it to this user's note ralation ship, which is the Note class
    