from flask import render_template, url_for, flash, redirect, request, jsonify
from sqlalchemy.exc import IntegrityError
from Aegis import app, db
from Aegis.models import Vaccination, County, Infected, State, County_exists, Vaccination_exists, Infected_exists
from datetime import date

import requests
import json 
from datetime import date

@app.route('/', methods=['GET', 'POST'])
def main():
	data = "state"
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
	
#DATABASE -----------------------------------------------------------------------------------------------

def reset_db():
	db.drop_all()
	db.session.commit()
	db.create_all()

def pulldata():
	# NY Times Data URLs
	counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
	# CDC API .json
	cdc_url = 'https://data.cdc.gov/resource/8xkx-amqh.json'
	# list of csv
	list_NYT = requests.get(counties_url).text.split('\n')
	# dict json.
	json_CDC = requests.get(cdc_url).json()
	
	for item in list_NYT[:-2:-1]:
		row = item.split(',')
		row[0] = date.fromisoformat(row[0])
		# county
		if not County_exists(row[3]):
			new_county = County(fips=row[3], state=row[3][0:2], name=row[1])
			db.session.add(new_county)
			db.session.commit()
			
		if not Infected_exists(row[3], row[0]):
			new_infected = Infected(fips=row[3], state=row[3][0:2], date=row[0], cases=int(row[4]), deaths=int(row[5]))
			db.session.add(new_infected)
			db.session.commit()
		
		
print("Running routes.py\n");
#pulldata()
#reset_db()

