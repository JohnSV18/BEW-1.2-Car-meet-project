from flask import Blueprint, request, render_template, redirect, url_for, flash, Flask
from app.models import CarEvent, Car, User
from app.forms import carEventForm, carForm, LoginForm, SignUpForm
from flask_login import login_required, login_user, logout_user, current_user
from flask_bcrypt import Bcrypt


from grocery_app import app, db

main = Blueprint('main', __name__)

bcrypt = Bcrypt(app)

@main.route('/')
def homepage():
    all_events = CarEvent.query.all()
    print(all_events)
    return render_template('home.html', all_events=all_events)

# Create your routes here.