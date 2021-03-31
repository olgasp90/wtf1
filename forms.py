from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField,SelectField
from flask_wtf.html5 import URLField
from wtforms.validators import InputRequired, Optional, NumberRange


class AddPetForm(FlaskForm):

    name = StringField('Name', validators=[InputRequired(message="Please add pet's name!")])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porc', 'Porcupine')], validators=[InputRequired()])
    photo_url = URLField('Image', validators=[Optional()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0,max=30, message='The age should be between 0 and 30')])
    notes = TextAreaField('Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = URLField('Image', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Available?')