from Aegis import db

class State(db.Model):
	state_id = db.Column(db.Integer, primary_key=True)
	#json = db.Column(db.Text)

class County(db.Model):
	fips = db.Column(db.String(5), primary_key=True)
	state = db.Column(db.Integer)
	name = db.Column(db.Text)
	#json = db.Column(db.Text)
	
class Vaccination(db.Model):
	fips = db.Column(db.String(5), db.ForeignKey('county.fips'), primary_key=True)
	state = db.Column(db.String(2))
	date = db.Column(db.Date, primary_key=True)
	full_vax = db.Column(db.Integer) # Series_Complete_Yes Total number of people who are fully vaccinated 
	percentage = db.Column(db.Float) # Percent of people who are fully vaccinated

class Infected(db.Model):
	fips = db.Column(db.String(5), db.ForeignKey('county.fips'), primary_key=True)
	state = db.Column(db.String(2))
	date = db.Column(db.Date, primary_key=True)
	cases = db.Column(db.Integer)
	deaths = db.Column(db.Integer)
	
	
def County_exists(pk):
	exists = db.session.query(County).filter_by(fips=pk).scalar() is not None
	if exists:
		#print("C already in db")
		return True
	return False
	
def Vaccination_exists(fips, date):
	exists = db.session.query(Vaccination).filter_by(fips=fips, date=date).scalar() is not None
	if exists:
		#print("Vax already in db")
		return True
	return False

def Infected_exists(fips, date):
	exists = db.session.query(Infected).filter_by(fips=fips, date=date).scalar() is not None
	if exists:
		#print("Inf already in db")
		return True
	return False