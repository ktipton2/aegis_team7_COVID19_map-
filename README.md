# COVID-19 Map

<h3>Team 7</h3>
Team roster: Kyle Tipton, Kelly Snyder, Pierce Jackson, ​
Ryan Orndoff, Johnathan Brown, Amy Phan

## About The Project

<i>You can use a windows or mac device for this application. </i>

**Languages and Tools:**
<p> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank"> <img src="https://d2knvm16wkt3ia.cloudfront.net/assets/svg-icon/flask.svg" alt="flask" width="40" height="40"/> </a><a href="https://www.mysql.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a></p>

**Extensions:**
- flask
- flask-sqlalchemy
- requests

**Data Sources**

<u>CDC API of COVID-19 Vaccinations in the United States, County​</u>

API that contains the vaccinations data of all counties.

https://data.cdc.gov/resource/8xkx-amqh.json

<u>New York Times Coronavirus (Covid-19) Data in the United States on GitHub​</u>

GitHub repo containing bot information as well as .csv files by state, by county for use as a dataset ; Live data versions updated several times each day​.

https://github.com/nytimes/covid-19-data    

<u>State geoJSON </u>

Code that adds custom overlays for states using D3 to render the GeoJSON shapes in conjunction with Leaflet. 

https://bost.ocks.org/mike/leaflet/ 

## To set up venv

**Windows:**

in the root folder (the one this file is in) run: 
```
py -m venv venv
```

to activate your venv: 
```
venv\Scripts\activate
```
make sure to pip install: 
python -m pip install 
```
flask
flask-sqlalchemy 
requests
```

**Mac:**

***Notice: Mac OS uses an older version of python, so you want to change it to at least python 3.6+ if you are unable to use the pip command***

1. Install Python 3.6+ which should come with pip. If you have python installed, check the version by typing:
```
python --version
```

If it lists out a python version less than 3.6+, then check out this page and follow the steps:
    https://stackoverflow.com/questions/1687357/updating-python-on-mac


2. Instal and activate virtualenv to check if you have correctly downloaded it:
```
sudo python3 -m pip install virtualenv
mkdir <project name>
cd <project name>
python3 -m venv <name of environment>
source <name of environment>/bin/activate
```

3. Once you've entered your virtualenv, do the following in the command line 

```
python -m pip install flask
python -m pip install flask-sqlalchemy
python -m pip install requests
```
4. Once you've installed these extensions, create a flask command that will be used to specify how to load the application <i>(assuming you're using bash, otherwise check out the [flask site](https://flask.palletsprojects.com/en/2.0.x/cli/)</i>:
```
$ export FLASK_APP=run
$ flask run
```
5. You should be able to run and open the application now.


####
