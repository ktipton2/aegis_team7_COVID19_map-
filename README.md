# COVID-19 Map

<h3>Team 7</h3>
Team roster: Kyle Tipton, Kelly Snyder, Pierce Jackson, ​
Ryan Orndoff, Johnathan Brown, Amy Phan

## Introduction:
Our product is a web-based map dashboard that will show the statistics of COVID-19 infections, vaccination, and death rates at a county level in the United States. Our software should show a map that will allow the user to choose a particular county that will show COVID-19 relevant data based on their choice of date and data type. Additionally, the dashboard will also show data graphs (bar graph).  

## About The Project

<i>You can use a windows or mac device for this application. </i>

**Languages and Tools:**
<p> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank"> <img src="https://d2knvm16wkt3ia.cloudfront.net/assets/svg-icon/flask.svg" alt="flask" width="40" height="40"/> </a><a href="https://www.sqlite.org/index.html" target="_blank"> <img src="https://user-images.githubusercontent.com/33158051/103467186-7b6a8900-4d1a-11eb-9907-491064bc8458.png" alt="sqlite" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a></p>

(HTML5/CSS3/Bootstrap/Flask/sqlite/Python)


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

<u>County geoJSON </u>

A dataset containing the GeoJSON shapes for US counties, as well as population data. This dataset is very large, our application uses a reduced precision version of the geoJSON, created using  mapshaper. 

https://hub.arcgis.com/datasets/esri::usa-counties/about 

https://mapshaper.org/ 

## Installation:

Go to our GitHub page and export our project files (clone/downloading the zip) into a workspace folder: 

https://github.com/ktipton2/aegis_team7_COVID19_map-  
 
Through terminal (or VSCode’s terminal), move into the workspace folder. From there, you can do the following steps to install the virtual environment and the rest of the dependents. From there you should be able to run the site: 

**Windows:**

1. Install python 3.6, which should come with pip. Follow the installation instructions and check if it’s correctly installed by typing: 
```
py –version 
```
2. Install and set up a virtualenv: 
```
sudo py –m pip install virtualenv 
mkdir <project name> 
cd<project name> 
py –m venv venv 
Call venv\Scripts\activate
```

3. Install the extensions 
```
py -m pip install flask 
py -m pip install flask-sqlalchemy 
py -m pip install requests 
```

4. Once you’ve installed these dependents, create a flask command that will be used to specify how to load the application (assuming you’re using bash, otherwise check out the flask site): 
```
// activate the python environment 
$ set FLASK_APP=run.py 
$ flask run 
```
(Make sure you’re within the aegis_team7_COVID19_map- folder) 

5. You should be able to run and open the application now. 

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
4. Once you've installed these dependents, create a flask command that will be used to specify how to load the application <i>(assuming you're using bash, otherwise check out the [flask site](https://flask.palletsprojects.com/en/2.0.x/cli/)</i>:
```
$ export FLASK_APP=run
$ flask run
```
(Make sure you’re within the aegis_team7_COVID19_map- folder)

5. You should be able to run and open the application now.


####
