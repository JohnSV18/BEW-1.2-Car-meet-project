from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtform.validators import DataRequired, Length

class carEventForm(FlaskForm):
    """For creating car meet events"""
    title = StringField('Car Name', validators=[DataRequired()])
    address = StringField('Car Event address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class carForm(FlaskForm):
    """For creating car that will be coming to car meet"""
    model_name = StringField('Car model', validators=[DataRequired()])
    make_name = StringField('Car make', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class SignUpForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

