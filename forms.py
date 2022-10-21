"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, Email, Length, URL


class AddPetForm(FlaskForm):
    "form for adding a new pet"

    name = StringField(
        "Pet name",
        validators=[
            InputRequired(),
            Length(min=-1, max=50,
                   message="Maximum length is 50 characters")
        ]
    )

    species = SelectField(
        "Species",
        choices=[
            ('cat', 'Cat'),
            ('dog', 'Dog'),
            ('porcupine', 'Porcupine')
        ],
        validators=[InputRequired()]
    )

    age = SelectField(
        "Age",
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
        ],
        validators=[InputRequired()]
    )

    notes = StringField(
        "Notes",
        validators=[
            InputRequired(),
            Length(min=-1, max=50, message="Maximum length is 50 characters")
        ]
    )
