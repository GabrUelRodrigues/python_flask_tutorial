from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	data = db.Column(db.String(10000))
	date = db.Column(db.DateTime(timezone=True), defaul=func.now())
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(150), unique=True)
	name = db.Column(db.String(150))
	password = db.Column(db.String(150))
	notes = db.relationship("Note")