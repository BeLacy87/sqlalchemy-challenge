import numpy as np
import datetime as dt
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
    session=Session(engine)
    results=session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    dict={}
    for i in results:
        dict.update({i[0]:i[1]})
    return jsonify(f"{dict}")

@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)
    result=session.query(Station.name).distinct()
    session.close()

    station=[]
    for i in result:
        station.append(i)
    return jsonify(f"{station}")

@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)

    most_recent_data_point=session.query(Measurement.date).\
        order_by((Measurement.date).desc()).first()[0]
    most_recent_date = dt.datetime.strptime(str(most_recent_data_point), '%Y-%m-%d').date()
    year_ago = most_recent_date - dt.timedelta(days=365)

    temp_obs=session.query(Measurement.date, Measurement.tobs).\
        filter(Station.station == Measurement.station).\
            filter(Measurement.date > year_ago).\
                filter(Station.id == 7).all()
    session.close()
    dict={}
    for i in temp_obs:
        dict.update({i[0]:i[1]})
    return jsonify(f"{dict}")

@app.route("/api/v1.0/<start>")
def start():
    return (f"test")

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return (f"test")


if __name__ == '__main__':
    app.run(debug=True)
