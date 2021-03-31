#import sql
from flask_sqlalchemy import SQLAlchemy


#execute sql alchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


DEFAULT_IMAGE = 'https://mediacloud.kiplinger.com/image/private/s--zFDKjwc_--/f_auto,t_primary-image-desktop@2/v1584618177/slideshow/investing/T052-S001-the-9-best-pure-bred-pet-stocks-to-buy/images/intro.jpg'


class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String, nullable=False)

    species = db.Column(db.String, nullable=False)

    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default=True)

    def pet_image(self):
        return self.photo_url or DEFAULT_IMAGE