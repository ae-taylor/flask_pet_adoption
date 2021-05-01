"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_wtf import FlaskForm

from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

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

@app.route("/")
def show_home():
    """show all pets on homepage"""

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route("/add", methods=["POST", "GET"])
def show_add_pet_form():
    """ render form to add pet """
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet()
        pet.name = form.name.data
        pet.species = (form.species.data).lower()
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        flash(f"Added {pet.name} to adoptable pets!")
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('add_pet_form.html', form=form)

    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_pet_details(pet_id):
    """ Shows pet details and form to edit pet """
    form = EditPetForm()
    pet = Pet.query.get_or_404(pet_id)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        flash(f"Updated {pet.name}!")
        return redirect(f"/{pet.id}")
    else:
        return render_template("pet_info.html", pet=pet, form=form)