from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, URL

class carEventForm(FlaskForm):
    """For creating car meet events"""
    title = StringField('Car Event', validators=[DataRequired()])
    address = StringField('Car Event address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class carForm(FlaskForm):
    """For creating car that will be coming to car meet"""
    model_name = StringField('Car model', validators=[DataRequired()])
    make_name = StringField('Car make', validators=[DataRequired()])
    photo_url = StringField('Photo', validators=[DataRequired(), URL(message='Must be a valid URL')])
    submit = SubmitField('Submit')
    