# Requirements to run:
# https://github.com/psf/requests
# https://github.com/pandas-dev/pandas
# To install required libraries use Linus cmds:
#     python -m pip install pandas
#     python -m pip install requests


import requests
import pandas as pd
import io
import json
import pickle

from requests.exceptions import HTTPError
from json.decoder import JSONDecodeError

# NY Times Data URLs
states_url = 'https://github.com/nytimes/covid-19-data/blob/4c29286b4fb6dbb515d69541f68b1e5831531075/live/us-states.csv'
counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

# CDC API .json
cdc_url = 'https://data.cdc.gov/resource/8xkx-amqh.json'

# This comes in as a .csv
resp_NYT = requests.get(counties_url).content

# This comes in as a .json
resp_CDC = requests.get(cdc_url).content

county_data_NYT = pd.read_csv(io.StringIO(resp_NYT.decode('utf-8')))
county_data_CDC = pd.read_json(io.StringIO(resp_CDC.decode('utf-8')))

# Save NYT data as a .json
county_data_NYT.to_json(r"county_data_NYT.json")

# Save CDC data as a .json
county_data_CDC.to_json(r"county_data_CDC.json")

# Save it as a Python dictionary
with open('county_data_NYT.json') as json_file:
    county_data_NYT = json.load(json_file)

    # Check if data variable is dict
    #print("Type: ", type(county_data_NYT))

    # Check data is present in dict
    #print(county_data_NYT)

    # Extra functionality:
    # Output dict into .pkl file
    NYT_pickle = open("county_data_NYT.pkl", "wb")
    pickle.dump(county_data_NYT, NYT_pickle)
    NYT_pickle.close()

with open('county_data_CDC.json') as json_file:
    county_data_CDC = json.load(json_file)

    # Check if data variable is dict
    #print("Type: ", type(county_data_CDC))

    # Check data is present in dict
    #print(county_data_CDC)

    # Extra functionality:
    # Output dict into .pkl file
    CDC_pickle = open("county_data_CDC.pkl", "wb")
    pickle.dump(county_data_CDC, CDC_pickle)
    CDC_pickle.close()
