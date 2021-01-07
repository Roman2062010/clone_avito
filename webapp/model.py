from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.Integer(12), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    role = db.Column(db.String(10)
    
    ads = db.relationship('Ad', backref='User')


class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    text = db.Column(db.Text(2000), nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    published = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    categoryone_id = db.Column(db.String, db.ForeignKey('CategoryOne.id'), nullable=False)
    categorytwo_id = db.Column(db.String, db.ForeignKey('CategoryTwo.id'), nullable=False)
    categorythree_id = db.Column(db.String, db.ForeignKey('CategoryThree.id'), nullable=False)
    categoryfour_id = db.Column(db.String, db.ForeignKey('CategoryFour.id'), nullable=False)
    location_id = db.Column(db.String, db.ForeignKey('Location.id'), nullable=False)


class CategoryOne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cat_1 = db.relationship('Ad', backref='CategoryOne')

    cat_1a = db.relationship('CategoryTwo', backref='CategoryOne')


class CategoryTwo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cat_2 = db.relationship('Ad', backref='CategoryTwo')

    category_1_id = db.Column(db.String, db.ForeignKey('CategoryOne.id'), nullable=False)
    
    cat_2a = db.relationship('CategoryThree', backref='CategoryTwo')


class CategoryThree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cat_3 = db.relationship('Ad', backref='CategoryThree')

    category_2_id = db.Column(db.String, db.ForeignKey('CategoryTwo.id'), nullable=False)

    cat_3a = db.relationship('CategoryFour', backref='CategoryThree')


class CategoryFour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cat_4 = db.relationship('Ad', backref='CategoryFour')

    category_3_id = db.Column(db.String, db.ForeignKey('CategoryThree.id'), nullable=False)
    
    
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    loc = db.relationship('Ad', backref='Location')