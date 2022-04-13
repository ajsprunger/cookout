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
    created_cookouts = db.relationship('Cookout', backref='creator', lazy=True)
    provided_food = db.relationship('Food', backref='provider', lazy=True)
    provided_drink = db.relationship('Drink', backref='provider', lazy=True)

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
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(150))
    food = db.relationship('Food', backref='event', lazy=True)
    drink = db.relationship('Drink', backref='event', lazy=True)
    attendees = db.Column(db.String)

    def __init__(self, name, date, creator_id, description, location, food, drink, attendees):
        self.name = name
        self.date = date
        self.creator_id = creator_id
        self.description = description
        self.location = location
        self.food = food
        self.drink = drink
        self.attendees = attendees

class Food(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('cookouts.id'), nullable=False)

    def __init__(self, name, provider_id, event_id):
        self.name = name
        self.provider_id = provider_id
        self.event_id = event_id


class Drink(db.Model):
    __tablename__ = 'drinks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('cookouts.id'), nullable=False)

    def __init__(self, name, provider_id, event_id):
        self.name = name
        self.provider_id = provider_id
        self.event_id = event_id


