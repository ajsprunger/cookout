from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired

class CookoutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    date = DateTimeLocalField('Date/Time', format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    location = StringField('Location')
    attendees = StringField('Attendees')
    submit = SubmitField('Create')

class FoodForm(FlaskForm):
    name = StringField('Add Food', validators=[DataRequired()])
    submit = SubmitField('Add')

class DrinkForm(FlaskForm):
    name = StringField('Add Drink', validators=[DataRequired()])
    submit = SubmitField('Add')

