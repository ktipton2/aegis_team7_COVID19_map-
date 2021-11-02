from flask import render_template, url_for, flash, redirect, request, jsonify
from sqlalchemy.exc import IntegrityError
from Aegis import app, db
from Aegis.models import County

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
    return jsonify(a)