from flask import render_template, url_for, flash, redirect, request
from sqlalchemy.exc import IntegrityError
from Aegis import app, db
from Aegis.models import State

@app.route('/', methods=['GET', 'POST'])
def main():
	data = "hello"
	if request.method == 'GET':
		data = request.args.get('state')
		print(data)
	return render_template('Choropleth Tutorial - Leaflet.html', title='Individual Assignment', data=data)
	
#@app.route('/<_data>', methods=['GET', 'POST'])
#def data(_data):
#		print(_data)
#helpers