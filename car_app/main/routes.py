from flask import Blueprint, request, render_template, redirect, url_for, flash, Flask
from car_app.models import Event, Car, User
from car_app.main.forms import EventForm, CarForm
from flask_login import login_required, login_user, logout_user, current_user
from flask_bcrypt import Bcrypt


from car_app import app, db

main = Blueprint('main', __name__)

bcrypt = Bcrypt(app)

@main.route('/')
def homepage():
    all_events = Event.query.all()
    print(all_events)
    return render_template('home.html', all_events=all_events)

@main.route('/new_event', methods=['GET', 'POST'])
@login_required 
def new_event():
    form=EventForm()

    if form.validate_on_submit():
        new_event= Event(
            title = form.title.data,
            description = form.description.data,
            address = form.address.data
        )
        db.session.add(new_event)
        db.session.commit()

        flash('You have Succesfully created a new car event')
        return redirect(url_for('main.event_detail', event_id=new_event.id))
    return render_template('new_event.html', form=form)

@main.route('/event/<event_id>', methods=['GET', 'POST'])
@login_required 
def event_detail(event_id):
    event = Event.query.get(event_id)
    form = EventForm(obj=event)
    
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.address = form.address.data

        db.session.commit()

        flash('You have Succesfully updated your event')
        return redirect(url_for('main.event_detail', event_id=event.id, event=event))
    return render_template('event_detail.html', event=event, form=form)

@main.route('/new_car', methods=['GET', 'POST'])
@login_required 
def new_car():
    form=CarForm()

    if form.validate_on_submit():
        new_car= Car(
            name = form.name.data,
            make_name = form.make_name.data,
            photo_url = form.photo_url.data,
            events = form.events.data
        )
        db.session.add(new_car)
        db.session.commit()

        flash('You have successfully added a new car to an event')
        return redirect(url_for('main.car_detail', car_id=new_car.id))
    return render_template('new_car.html', form=form)

@main.route('/car/<car_id>', methods=['GET', 'POST'])
@login_required 
def car_detail(car_id):
    car = Car.query.get(car_id)
    form = CarForm(obj=car)
    
    if form.validate_on_submit():
        car.name = form.name.data
        car.make_name = form.make_name.data
        car.photo_url = form.photo_url.data

        db.session.commit()

        flash('You have Succesfully updated your car')
        return redirect(url_for('main.car_detail', car_id=car.id, car=car))
    return render_template('car_detail.html', car=car, form=form)

@main.route('/car_show/<event_id>', methods=['GET', 'POST'])
def car_show(event_id):
    event = Event.query.get(event_id)

    return render_template('car_show.html', event=event)