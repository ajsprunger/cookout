#models 
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime, timedelta

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    cookouts = db.relationship('Cookout', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"

class Cookout(db.Model):
    __tablename__ = 'cookouts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    name = db.Column(db.String(100), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(150))
    food = db.Column(db.String)
    drink = db.Column(db.String)
    attendees = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, date, creator, location, food, drink, attendees):
        self.name = name
        self.date = date
        self.creator = creator
        self.location = location
        self.food = food
        self.drink = drink
        self.attendees = attendees