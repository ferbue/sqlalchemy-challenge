import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def homepage():
    return (
        "Welcome to the Weather API!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/&lt;start&gt;<br/>"
        "/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Your code to calculate and return precipitation data as JSON
    pass

@app.route("/api/v1.0/stations")
def stations():
    # Your code to retrieve and return station data as JSON
    pass

@app.route("/api/v1.0/tobs")
def tobs():
    # Your code to retrieve and return temperature observation data as JSON
    pass

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp_stats(start, end=None):
    # Your code to calculate and return temperature statistics as JSON
    pass

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
