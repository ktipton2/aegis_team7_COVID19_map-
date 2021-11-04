import requests
import json 

# NY Times Data URLs
counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

# CDC API .json
cdc_url = 'https://data.cdc.gov/resource/8xkx-amqh.json'

# list of csv
list_NYT = requests.get(counties_url).text.split('\n')

# dict json.
json_CDC = requests.get(cdc_url).json()

print(json_CDC[-1]['date'][0:10])

#date,county,state,fips,cases,deaths
print(list_NYT[-1].split(','))
	
for item in json_CDC[:-10:-1]:
		print(item['date'][0:10])

for item in list_NYT[:-10:-1]:
		print(item.split(','))
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