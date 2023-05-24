from . import db
from sqlalchemy import LargeBinary
from sqlalchemy.sql import func

class Opinion(db.Model):
    __tablename__ = 'opinions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    opinion = db.Column(db.String(500), nullable=False)

class Hairdresser(db.Model):
    __tablename__ = 'hairdressers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    picture = db.Column(LargeBinary)

class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(10), nullable=False)