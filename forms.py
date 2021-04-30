from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    name = StringField("Name:")
    species = StringField("Species:")
    photo_url = StringField("Photo Url:")
    age = SelectField(
        'Age',
        choices = [('baby', 'baby'), 
                    ('young', 'young'), 
                    ('adult', 'adult'), 
                    ('senior', 'senior')]
        )
    notes = StringField("Notes:")
    available = BooleanField('Available')