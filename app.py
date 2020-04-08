import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Station=Base.classes.station
Measurement=Base.classes.measurement

app = Flask(__name__)

@app.route("/")
def home_page():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    return (f"test")

@app.route("/api/v1.0/stations")
def stations():
    return (f"test")

@app.route("/api/v1.0/tobs")
def tobs():
    return (f"test")

@app.route("/api/v1.0/<start>")
def start():
    return (f"test")

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return (f"test")


if __name__ == '__main__':
    app.run(debug=True)
