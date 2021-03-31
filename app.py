from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'YOU_WILL_NEVER_GUESS'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def home():

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    print(request.form)
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()
        flash(f'Pet {name} was added!')

        return redirect('/')
    else:
        return render_template('pet_form.html', form = form)

@app.route('/<int:id>')
def show_pet_info(id):
    pet = Pet.query.get_or_404(id)
    return render_template('pet.html', pet=pet)


@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        db.session.commit()
        flash(f'{pet.name} updated!')

        return redirect('/')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)


@app.route('/<int:id>/delete', methods=['POST'])
def delete_pet(id):
    pet = Pet.query.get_or_404(id)

    db.session.delete(pet)
    db.session.commit()
    flash(f'{pet.name} has been deleted')
    return redirect('/')
