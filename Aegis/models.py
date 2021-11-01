from Aegis import db

class State(db.Model):
	state_id = db.Column(db.Integer, primary_key=True)
	json = db.Column(db.Text)

class County(db.Model):
	fips = db.Column(db.Integer, primary_key=True)
	json = db.Column(db.Text)
	
class Vaccination(db.Model):
	fips = db.Column(db.Integer, db.ForeignKey('County.fips'), primary_key=True,)
	date = db.Column(db.Date, primary_key=True)
	full_vax = db.Column(db.Integer)

class Infected(db.Model):
	fips = db.Column(db.Integer, db.ForeignKey('County.fips'), primary_key=True)
	date = db.Column(db.Date, primary_key=True)
	cases = db.Column(db.Integer)
	deaths = db.Column(db.Integer)