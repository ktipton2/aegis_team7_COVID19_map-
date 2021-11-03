from Aegis import db

class State(db.Model):
	state_id = db.Column(db.Integer, primary_key=True)
	json = db.Column(db.Text)

class County(db.Model):
	fips = db.Column(db.String(5), primary_key=True)
	state = db.Column(db.Integer)
	json = db.Column(db.Text)
	
class Vaccination(db.Model):
	fips = db.Column(db.String(5), db.ForeignKey('county.fips'), primary_key=True)
	state = db.Column(db.String(2))
	date = db.Column(db.Date, primary_key=True)
	full_vax = db.Column(db.Integer)

class Infected(db.Model):
	fips = db.Column(db.String(5), db.ForeignKey('county.fips'), primary_key=True)
	state = db.Column(db.String(2))
	date = db.Column(db.Date, primary_key=True)
	cases = db.Column(db.Integer)
	deaths = db.Column(db.Integer)