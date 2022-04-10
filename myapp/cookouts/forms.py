from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField, SelectField
from wtforms.validators import DataRequired

class CookoutPostForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    date = DateTimeField('Date', validators=[DataRequired()])
    location = StringField('Location')
    food = StringField('Food')
    drink = StringField('Drink')
    attendees = SelectField('Attendees')
    submit = SubmitField('Post')