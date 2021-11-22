from Aegis import db

class State(db.Model):
	state = db.Column(db.String(2), primary_key=True)
	name = db.Column(db.Text)

class County(db.Model):
	fips = db.Column(db.String(5), primary_key=True)
	state = db.Column(db.String(2))
	name = db.Column(db.Text)
	population = db.Column(db.Integer)
	
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
	
def State_exists(pk):
	exists = db.session.query(State).filter_by(state=pk).scalar() is not None
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