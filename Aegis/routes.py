from flask import render_template, url_for, flash, redirect, request, jsonify
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from Aegis import app, db
from Aegis.models import Vaccination, County, Infected, State, County_exists, Vaccination_exists, Infected_exists, State_exists
from datetime import date, timedelta
import requests
import json 
import time

DEFAULT_DATE_STRING = '2021-12-04'

end_date =  date.fromisoformat(DEFAULT_DATE_STRING)
start_date = end_date - timedelta(days=1)
table = "Vaccination"

# the main page. called whenever the site is visted. 
@app.route('/', methods=['GET', 'POST'])
def main():
	global end_date
	
	maxDate = db.session.query(func.max(Vaccination.date)).first()
	minDate = db.session.query(func.min(Vaccination.date)).first()

	#print(type(maxDate[0]))
	#print(type(start_date))
	
	return render_template('Group 7 Map.html', defaultDateStart=start_date, defaultDateEnd=end_date, maxStartDate=maxDate[0], minStartDate=minDate[0], maxEndDate=maxDate[0], minEndDate=start_date+timedelta(days=1))

@app.route('/setDate', methods=['GET', 'POST'])
def setDate():
	global end_date
	global start_date
	start_date = date.fromisoformat(request.args.get('chosenDateStart'))
	end_date = date.fromisoformat(request.args.get('chosenDateEnd'))

	return "Date has been changed!"
	
# data is sent from the client when they click on a state
# a query is made
# data is sent back in json format
@app.route('/geojson-features', methods=['GET'])
def fe_request_by_state():
	global end_date
	global start_date
	state = request.args.get('state')
	table = request.args.get('table')
	
	#print(start_date, end_date)
	
	#days between end_date and start_date
	delta = (end_date - start_date).days
	
	# the data to be returned
	dict = {}
	
	# the population per county
	county_dict = {}
	
	result = ""

	# end date - start date
	if table == "Vaccination":	
		Q1 = Vaccination.query.filter_by(state=state, date=end_date).all()
		Q2 = Vaccination.query.filter_by(state=state, date=start_date).all()
			
		for row in Q1:
			dict[row.fips] = row.full_vax
		
		if start_date != end_date:
			for row in Q2:
				if row.fips in dict:
					dict[row.fips] -= row.full_vax	
				
	elif table == "Infection-Cases":
		Q1 = Infected.query.filter_by(state=state, date=end_date).all()
		Q2 = Infected.query.filter_by(state=state, date=start_date).all()
		for row in Q1:
			dict[row.fips] = row.cases
		
		if start_date != end_date:	
			for row in Q2:
				if row.fips in dict:
					dict[row.fips] -= row.cases	
	else:
		Q1 = Infected.query.filter_by(state=state, date=end_date).all()
		Q2 = Infected.query.filter_by(state=state, date=start_date).all()
	
		for row in Q1:
			dict[row.fips] = row.deaths
			
		if start_date != end_date:	
			for row in Q2:
				if row.fips in dict:
					dict[row.fips] -= row.deaths
				
		
	#print(dict.keys())
	population = County.query.filter_by(state=state).all();
	for row in population:
		county_dict[row.fips] = row.population 
	
	if start_date == end_date:
		delta = 1
		
	# Per Capita Calculation by Current Feature
	for key in dict:
		try: 
			dict[key] = round((dict[key] / delta) / county_dict[key] * 100000, 2)
		except:
			# keys not in county_dict
			print(key)
			dict[key] = None
	
	return jsonify({"data" : dict})
	
#DATABASE -----------------------------------------------------------------------------------------------
@app.route('/update-database', methods=['GET'])
def fe_update_database():
	print("pulling data: may take some time")
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
	#&$offset=150000
	
	# list of csv
	list_NYT = requests.get(counties_url, headers={"content-type":"text"}).text.split('\n')
	# dict json.
	json_CDC = requests.get(cdc_url).json()
	
	#counties data
	with open('Aegis/static/USA_Counties_Reduced_2P.json') as dataFile:
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
		#print(row)
		#exit if not 2021
		if((row[0][:7] != '2021-12') and (row[0][:7] != '2021-11')):
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
		if(item['date'][:7] != '2021-11' and item['date'][:7] != '2021-12'):
			break;
			
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
