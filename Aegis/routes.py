from flask import render_template, url_for, flash, redirect, request, jsonify
from sqlalchemy.exc import IntegrityError
from Aegis import app, db
from Aegis.models import Vaccination, County, Infected, State, County_exists, Vaccination_exists, Infected_exists, State_exists
from datetime import date, timedelta

import requests
import json 

import time

end_date =  date.fromisoformat('2021-11-04')
table = "Vaccination"

# the main page. called whenever the site is visted. 
@app.route('/', methods=['GET', 'POST'])
def main():
	global end_date
	return render_template('Group 7 Map.html', date=end_date)

@app.route('/setDate', methods=['GET', 'POST'])
def setDate():
	global end_date
	end_date = date.fromisoformat(request.args.get('chosenDate'))

	return "Date has been changed!"
	
# data is sent from the client when they click on a state
# a query is made
# data is sent back in json format
@app.route('/geojson-features', methods=['GET'])
def fe_request_by_state():
	global end_date
	start_date = end_date - timedelta(days=1)
	state = request.args.get('state')
	table = request.args.get('table')
	
	dict = {}
	result = ""
	#dict['table'] = table
	
	if table == "Vaccination":	
		Q1 = Vaccination.query.filter_by(state=state, date=end_date).all()
		Q2 = Vaccination.query.filter_by(state=state, date=start_date).all()
		
		for row in Q1:
			dict[row.fips] = row.full_vax
		
		for row in Q2:
			if row.fips in dict:
				dict[row.fips] -= row.full_vax	
		
	elif table == "Infection-Cases":
		Q1 = Infected.query.filter_by(state=state, date=end_date).all()
		Q2 = Infected.query.filter_by(state=state, date=start_date).all()
	
		for row in Q1:
			dict[row.fips] = row.cases
			
		for row in Q2:
			if row.fips in dict:
				dict[row.fips] -= row.cases	
	else:
		Q1 = Infected.query.filter_by(state=state, date=end_date).all()
		Q2 = Infected.query.filter_by(state=state, date=start_date).all()
	
		for row in Q1:
			dict[row.fips] = row.deaths
			
		for row in Q2:
			if row.fips in dict:
				dict[row.fips] -= row.deaths	
				
	return jsonify({"data" : dict})
	
#DATABASE -----------------------------------------------------------------------------------------------
@app.route('/update-database', methods=['GET'])
def fe_update_database():
	print("pulling data")
	#reset_db()
	start_time = time.time()
	pulldata()
	print("done")
	print("--- %s seconds ---" % (time.time() - start_time))
	return jsonify({"data" : True}) 

def reset_db():
	db.drop_all()
	db.session.commit()
	db.create_all()

def pulldata():
	# NY Times Data URLs
	counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
	# CDC API .json
	cdc_url = 'https://data.cdc.gov/resource/8xkx-amqh.json?$limit=50000'
	# list of csv
	list_NYT = requests.get(counties_url, headers={"content-type":"text"}).text.split('\n')
	# dict json.
	json_CDC = requests.get(cdc_url).json()
	
	#counties data
	with open('Aegis/static/USA_Counties.geojson') as dataFile:
		data = dataFile.read()
		obj = data[data.find('{') : data.rfind('}')+1]
		countiesData = json.loads(obj)
	
	#County.query.delete()
	#db.session.commit()
	
	print("files opened - now inserting")
	
	
	for item in countiesData['features']:
		if not State_exists(item['properties']['STATE_FIPS']):
			new_state = State(state=item['properties']['STATE_FIPS'], name=item['properties']['STATE_NAME'], )
			db.session.add(new_state)
	
		if not County_exists(item['properties']['FIPS']):
			new_county = County(fips=item['properties']['FIPS'], state=item['properties']['STATE_FIPS'], name=item['properties']['NAME'], population=item['properties']['POPULATION'] )
			db.session.add(new_county)
	
	db.session.commit()
	
	
	for item in list_NYT[::-1]:
		row = item.split(',')
		
		#exit if not 2021
		if(row[0][:7] != '2021-11'):
			break;
		
		if (len(row) != 6):
			continue;
		
		if(row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '' or row[5] == ''):
			continue;
		
		row[0] = date.fromisoformat(row[0])		
		
		if not Infected_exists(row[3], row[0]):
			new_infected = Infected(fips=row[3], state=row[3][0:2], date=row[0], cases=int(row[4]), deaths=int(row[5]))
			db.session.add(new_infected)
		
	db.session.commit()
	
	for item in json_CDC[::-1]:
		if(item['date'][:7] != '2021-11'):
			continue;
			
		if County_exists(item['fips']):
			if not Vaccination_exists(item['fips'], date.fromisoformat(item['date'][0:10])):
				new_vax = Vaccination(fips=item['fips'], state=item['fips'][0:2], 
									date=date.fromisoformat(item['date'][0:10]), 
									full_vax=int(item['series_complete_yes']), 
									percentage=float(item['series_complete_pop_pct']))
				db.session.add(new_vax)
	
	db.session.commit()
	
print("Running routes.py\n");
#reset_db()
#pulldata()
#print("data pulled");

# days between two date objects
#delta = d1 - d0
#print(delta.days)
