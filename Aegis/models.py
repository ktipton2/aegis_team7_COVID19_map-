from Aegis import db

# Table of items
class Item(db.Model):
	name = db.Column(db.String(50), nullable=False)
	id = db.Column(db.Integer, primary_key=True)
	points = db.Column(db.Integer)