from flask import render_template, url_for, flash, redirect, request, jsonify
from sqlalchemy.exc import IntegrityError
from Aegis import app, db
from Aegis.models import Vaccination, County, Infected, State, County_exists, Vaccination_exists, Infected_exists
from datetime import date, timedelta

import requests
import json 
from datetime import date

end_date =  date.fromisoformat('2021-11-04')
start_date = end_date + timedelta(days=1)

@app.route('/', methods=['GET', 'POST'])
def main():
	data = "state"
	return render_template('Choropleth Tutorial - Leaflet.html', title='Individual Assignment')
	
@app.route('/geojson-features', methods=['GET'])
def fe_request_by_state():
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
		
		#exit if not 2021
		if(row[0][:4] != '2021'):
			break;
		
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
		
	for item in json_CDC[:-2:-1]:
		if(item['date'][0:4] != '2021'):
			break;
		
		if County_exists(item['fips']):
			new_vax = Vaccination(fips=item['fips'], state=item['fips'][0:2], 
								date=date.fromisoformat(item['date'][0:10]), 
								full_vax=int(item['series_complete_yes']), 
								percentage=float(item['series_complete_pop_pct']))
			db.session.add(new_vax)
			db.session.commit()
		
print("Running routes.py\n");
#reset_db()
#pulldata()

# days between two date objects
#delta = d1 - d0
#print(delta.days)
