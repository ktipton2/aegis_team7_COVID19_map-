from flask import render_template, url_for, flash, redirect, request
from sqlalchemy.exc import IntegrityError
from Aegis import app, db
from Aegis.models import Item

@app.route('/', methods=['GET', 'POST'])
def main():

	return render_template('main.html', title='Individual Assignment')