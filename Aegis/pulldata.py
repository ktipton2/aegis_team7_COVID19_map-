import requests
import json 
from datetime import date, datetime
# NY Times Data URLs
counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

# CDC API .json
cdc_url = 'https://data.cdc.gov/resource/8xkx-amqh.json'

# list of csv
list_NYT = requests.get(counties_url).text.split('\n')

# dict json.
json_CDC = requests.get(cdc_url).json()

#print(json_CDC[-1]['administered_dose1_recip_12pluspop_pct'])

#date,county,state,fips,cases,deaths
#print(list_NYT[-1].split(','))
	
#3283 counties?

print("date,county,state,fips,cases,deaths")
count = 0;
for item in list_NYT[::-1]:
	row = item.split(',')
	count += 1
	if(row[0][:4] != '2021'):
		break;

print(count)

for item in json_CDC[:-10:-1]:
	if item['fips'] != "UNK":
		print([date.fromisoformat(item['date'][0:10]), item['fips'], item['series_complete_yes'] ])
		new_vax = Vaccination(fips=item['fips'], state=item['fips'][0:2], date=item['date'][0:10], full_vax=item['series_complete_yes'], percentage=item['series_complete_pop_pct'])
		#print(item['date'][0:10])
		#print(item['fips'])
		#print(item['series_complete_yes'])

#for item in list_NYT[:-10:-1]:
#		print(item.split(','))


#ROC = ((Q['series_complete_yes'] /  Q2['series_complete_yes']) -1) * 100

#X per time scale.
#per day, per week.

#rate = Q['series_complete_yes'] -  Q2['series_complete_yes']) / days

#new cases per timefram
#def get_or_create(cls, name):
#    exists = db.session.query(Employee.id).filter_by(name=name).scalar() is not None
#    if exists:
#        return db.session.query(Employee).filter_by(name=name).first()
#    return cls(name=name)

#new_vax = Vaccination(fips='00000', state='48', date=date.fromisoformat('2019-12-04'), full_vax=5)
#new_county = County 
#new_infected = Infected

#create the user for the db
#db.session.add(vax) #stage the user for the db
#db.session.commit() #commit new user to db
#print(resp_NYT)
#print(type(resp_NYT.text))
#print(type(resp_NYT.content))

#print(resp_CDC)
#print(type(resp_CDC.text))
#print(type(resp_CDC.content))