from flask import render_template, url_for, flash, redirect, request, jsonify
from sqlalchemy.exc import IntegrityError
from Aegis import app, db
from Aegis.models import Vaccination, County, Infected, State
from datetime import date

@app.route('/', methods=['GET', 'POST'])
def main():
	data = "hello"
	if request.method == 'GET':
		data = request.args.get('state')
		print(data)
	return render_template('Choropleth Tutorial - Leaflet.html', title='Individual Assignment')
	
@app.route('/geojson-features', methods=['GET'])
def get_all_points():
	a = request.args.get('state')
	data = Vaccination.query.filter_by(state=a).all()
	result = ""
	for row in data:
		result += row.fips
	return jsonify(result)

   
   
#fips = db.Column(db.Integer, db.ForeignKey('County.fips'), #primary_key=True,)
#	date = db.Column(db.Date, primary_key=True)
#	full_vax = db.Column(db.Integer)

#db.create_all()

#vax = Vaccination(fips='00000', state='48', date=date.fromisoformat('2019-12-04'), full_vax=5) #create the user for the db
#db.session.add(vax) #stage the user for the db
#db.session.commit() #commit new user to db

