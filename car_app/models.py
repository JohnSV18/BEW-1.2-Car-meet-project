from car_app import db
from sqlalchemy_utils import URLType
from flask_login import UserMixin

class Event(db.Model):
    """Car Meet Event Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    cars = db.relationship('Car', back_populates = 'events')

    def __repr__(self):
        return self.title

class Car(db.Model):
    """Car Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    make_name = db.Column(db.String(80), nullable=False)
    photo_url = db.Column(URLType)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    events = db.relationship('Event', back_populates='cars')
    

class User(db.Model, UserMixin):
    """User Item"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
