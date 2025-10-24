import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    boite_postale = db.Column(db.String(20), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    pays = db.Column(db.String(100), nullable=False)
    dates = db.Column(db.DateTime, nullable=True)
    def __repr__(self):
        return f"<Client {self.nom} {self.prenom}>"
