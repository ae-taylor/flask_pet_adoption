from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    name = StringField("Name:")
    species = SelectField("Species:",
            choices=[("dog", "dog"), ("cat", "cat"), ("porcupine", "porcupine")])
    photo_url = StringField("Photo Url:", validators=[Optional(), URL()])
    age = SelectField(
        'Age',
        choices = [('baby', 'baby'),
                    ('young', 'young'),
                    ('adult', 'adult'),
                    ('senior', 'senior')]
        )
    notes = StringField("Notes:")
    available = BooleanField('Available')
