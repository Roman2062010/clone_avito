from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone_number = dbColumn(db.Integer(11), index=True, unique=True, nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    role = db.Column(db.String(10), index=True)

    ads = db.relationship('Ad', backref='User')


class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    text = db.Column(db.Text(2000), nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    published = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    category_1_id = db.Column(db.String, db.ForeignKey('Ad_category_1.id'), nullable=False)
    category_2_id = db.Column(db.String, db.ForeignKey('Ad_category_2.id'), nullable=False)
    category_3_id = db.Column(db.String, db.ForeignKey('Ad_category_3.id'), nullable=False)
    category_4_id = db.Column(db.String, db.ForeignKey('Ad_category_4.id'), nullable=False)
    location_id = db.Column(db.String, db.ForeignKey('Location.id'), nullable=False)


class Ad_category_1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cat_1 = db.relationship('Ad', backref='Ad_category_1')

    cat_1a = db.relationship('Ad_category_2', backref='Ad_category_1')


class Ad_category_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cat_2 = db.relationship('Ad', backref='Ad_category_2')

    category_1_id = db.Column(db.String, db.ForeignKey('Ad_category_1.id'), nullable=False)
    
    cat_2a = db.relationship('Ad_category_3', backref='Ad_category_2')


class Ad_category_3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cat_3 = db.relationship('Ad', backref='Ad_category_3')

    category_2_id = db.Column(db.String, db.ForeignKey('Ad_category_2.id'), nullable=False)

    cat_3a = db.relationship('Ad_category_4', backref='Ad_category_3')


class Ad_category_4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cat_4 = db.relationship('Ad', backref='Ad_category_4')

    category_3_id = db.Column(db.String, db.ForeignKey('Ad_category_3.id'), nullable=False)
    
    
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    loc = db.relationship('Ad', backref='Location')