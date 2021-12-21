#import dependancies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# set up database
engine = create_engine("sqlite:///hawaii.sqlite")

# set base to access & query SQLite db file
Base = automap_base()

# reflect db
Base.prepare(engine, reflect=True)

# create variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link from python to db
session = Session(engine)

# set up flask & routes
app = Flask(__name__)

# create welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


