from flask import Blueprint, request, render_template, redirect, url_for, flash, Flask
from car_app.models import CarEvent, Car, User
from car_app.main.forms import carEventForm, carForm
from flask_login import login_required, login_user, logout_user, current_user
from flask_bcrypt import Bcrypt


from car_app import app, db

main = Blueprint('main', __name__)

bcrypt = Bcrypt(app)

@main.route('/')
def homepage():
    all_events = CarEvent.query.all()
    print(all_events)
    return render_template('home.html', all_events=all_events)

@main.route('/new_car', methods=['GET','POST'])
@login_required 
def new_car():
    form=carForm()

    if form.validate_on_submit():
        new_car = Car(
            model_name = form.model_name.data,
            make_name = form.make_name.data,
            photo_url = form.photo_url.data
        )
        db.session.add(new_car)
        db.session.commit()

        flash('You have Succesfully registered your car')
        return redirect(url_for('main.new_car', car_id=new_car.id))
    return render_template('new_car.html', form=form)

@main.route('/new_event', methods=['GET','POST'])
@login_required 
def new_event():
    form=carEventForm()

    if form.validate_on_submit():
        new_event = CarEvent(
            title= form.title.data,
            address = form.address.data,
        )
        db.session.add(new_event)
        db.session.commit()

        flash('You have Succesfully created a car meet event!')
        return redirect(url_for('main.new_event', event_id=new_event.id))
    return render_template('new_event.html', form=form)

