"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash, request

from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    """ Renders html to show pets list """
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Pet add form; handles adding a pet. When a new
    pet is added, redirects user to pet list page"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)

        db.session.add(pet)
        db.session.commit()
        flash(f'Added {name} to Pet Directory')
        return redirect('/')

    else:
        return render_template(
            'pet_add_form.html',
            form=form
        )


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_profile(pet_id):
    """ Renders HTML to view pet profile. User can edit pet profile and
    redirects user to the pet list"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    # breakpoint()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        availability = form.available.data
        pet.available = True if availability == "True" else False
        db.session.commit()
        flash(f'{pet.name} has been updated!')
        return redirect('/')

    else:
        return render_template(
            'pet_profile.html',
            pet=pet,
            form=form
        )
