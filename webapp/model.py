from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    role = db.Column(db.String(10))
    

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    text = db.Column(db.Text(2000), nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    published = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    categoryone_id = db.Column(db.Integer, db.ForeignKey('category_one.id'), nullable=False)
    categorytwo_id = db.Column(db.Integer, db.ForeignKey('category_two.id'), nullable=True)
    categorythree_id = db.Column(db.Integer, db.ForeignKey('category_three.id'), nullable=True)
    categoryfour_id = db.Column(db.Integer, db.ForeignKey('category_four.id'), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    image = db.Column(db.String)
    user = db.relationship("User", backref="ad")
    location = db.relationship("Location", backref="ad")
    categoryone = db.relationship("CategoryOne", backref="ad")


class CategoryOne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class CategoryTwo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class CategoryThree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class CategoryFour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)