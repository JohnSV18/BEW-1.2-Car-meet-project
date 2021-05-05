# Create your models here.
from car_app import db
from sqlalchemy_utils import URLType
from flask_login import UserMixin

class CarEvent(db.Model):
    """Car Meet Event Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)

class Car(db.Model):
    """Car Model"""
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(80), nullable=False)
    make_name = db.Column(db.String(80), nullable=False)
    photo_url = db.Column(URLType)

class User(db.Model, UserMixin):
    """User Item"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)