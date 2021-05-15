from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from car_app.models import Car, Event, User

class EventForm(FlaskForm):
    """For creating car meet events"""
    title = StringField('Car Event', validators=[DataRequired()])
    address = StringField('Car Event address', validators=[DataRequired()])
    description = StringField('Car Event Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CarForm(FlaskForm):
    """For creating car that will be coming to car meet"""
    name = StringField('Car model', validators=[DataRequired()])
    make_name = StringField('Car make', validators=[DataRequired()])
    photo_url = StringField('Photo', validators=[DataRequired(), URL(message='Must be a valid URL')])
    events = QuerySelectField('Events', query_factory=lambda: Event.query)
    submit = SubmitField('Submit')
    