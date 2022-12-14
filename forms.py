"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Optional, Length, URL


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

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
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

    notes = TextAreaField(
        "Notes",
        validators=[
            InputRequired(),
            Length(min=-1, max=50, message="Maximum length is 50 characters")
        ]  # can remove min parameter
    )


class EditPetForm(FlaskForm):
    """ Form for editing pet information """

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    notes = TextAreaField(
        "Notes",
        validators=[
            InputRequired(),
            Length(min=-1, max=50, message="Maximum length is 50 characters")
        ]
    )

    available = RadioField(
        "Pet Availability",
        choices=[
            ('True', 'Available'),
            ('False', 'Not Available'),
        ],
        # coerce=lambda x: x == 'True',
        validators=[InputRequired()]
    )
    #
