from matplotlib import style
style.use('seaborn')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt

# Reflect Tables into SQLAlchemy ORM

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
conn = engine.connect()

data = pd.read_sql("SELECT * FROM Measurement",conn)
data.head()

# Exploratory Climate Analysis

# Design a query to retrieve the last 12 months from 08-23-2017 of precipitation data and plot the results
# Getting "Javascript Error: IPython is not defined" error? Tried plt.bar() and df.plot.bar(). Runs in Jupyter Notebook, not Lab.

precip_data = pd.read_sql("SELECT date,prcp FROM Measurement GROUP BY date ORDER BY date DESC LIMIT 365", conn)
dates=precip_data["date"]
rain=precip_data["prcp"]

fig, ax = plt.subplots()
ax.bar(dates, rain)
ax.set_xlabel("Rain")
ax.set_ylabel("Inches")
ax.set_title("Observed Rain by Day - 8/24/16-8/23/17")
fig.tight_layout()
plt.show()

# Use Pandas to calcualte the summary statistics for the precipitation data
precip_data.describe()

# How many stations are available in this dataset?
stations_data = pd.read_sql("SELECT * FROM Station", conn)
len(stations_data)

# * Design a query to find the most active stations.
#   * List the stations and observation counts in descending order.
# should sum precip and temp observations for total activity? Sorted by Temp_Observations as that aligned with provided answer.

activity_data = pd.read_sql("SELECT station as Station,count(prcp) as Precip_Observations, count(tobs) as Temp_Observations FROM Measurement GROUP BY station ORDER BY Temp_Observations DESC", conn)
activity_data

# * Which station has the highest number of observations?
# Station USC00519281

top_data = pd.read_sql("SELECT station as Station,count(tobs) as Temp_Observations FROM Measurement GROUP BY station ORDER BY Temp_Observations DESC LIMIT 1", conn)
top_data

# * Design a query to retrieve the last 12 months of temperature observation data (tobs).

# select station,tobs from hawaii_measurements

#   * Filter by the station with the highest number of observations.

# select station,tobs from hawaii_measurements
# USC00519281
temp_data = pd.read_sql("SELECT station,date, tobs as Temperature_Observations FROM Measurement ORDER BY date DESC LIMIT 2223", conn)
top_data_year=temp_data.loc[temp_data["station"]=="USC00519281"]
top_data_year.tail()


#   * Plot the results as a histogram with `bins=12`.
# Getting "Javascript Error: IPython is not defined" error? Tried plt.bar() and df.plot.bar(). Runs in Jupyter Notebook, not Lab.

histogram=top_data_year.hist(column="Temperature_Observations", grid=True, bins=12)
top_tobs=top_data_year["Temperature_Observations"]
plt.hist(top_tobs,bins=12)
plt.show()

# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?

np.mean(top_tobs)
#73

max(top_tobs)
#83

min(top_tobs)
#59

print("Max Temp: 83")
print("Min Temp: 59")
print("Avg Temp: 73")

# Step 2 - Climate App

# Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.
from flask import Flask, jsonify

# * Use FLASK to create your routes.
app = Flask(__name__)

# Testing connection
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Now we're getting somewhere"

# * `/api/v1.0/precipitation`

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all precip"""
#   * Query for the dates and precip observations from the last year.
    results = session.query(Measurement.prcp).all()
    all_precip = list(np.ravel(results))
    return jsonify(all_precip)


#   * Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.
#   * Return the JSON representation of your dictionary.

""" NOTE: I can get the data for any single field (tobs, prcp, etc.) to query and jsonify, but couldn't get the
a dictionary to build to work and jsonify. I tried multiple variations on querying specific fields, 
the whole table, and combinations thereof. I think it's as much a Python issue as a querying issue,
unfortunately. Is that right? I've included a little of the code I tried for context, in addition
to the above"""

    # data2 = pd.read_sql("SELECT tobs FROM Measurement",conn)

    # all_temps = []
    # for temp in results:
    #     temp_dict = {}
    #     temp_dict["date"] = Measurement.date
    #     temp_dict["temp"] = Measurement.tobs
    #     all_temps.append(date_dict)
    # all_temps2 = list(np.ravel(data2))
    

if __name__ == "__main__":
    app.run(debug=False)

# @app.route("/api/v1.0/tobs")
# def passengers():
#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger).all()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for passenger in results:
#         passenger_dict = {}
#         passenger_dict["name"] = passenger.name
#         passenger_dict["age"] = passenger.age
#         passenger_dict["sex"] = passenger.sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)

#   * Query for the dates and temperature observations from the last year.

#   * Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.

#   * Return the JSON representation of your dictionary.

# * `/api/v1.0/stations`

#   * Return a JSON list of stations from the dataset.

# * `/api/v1.0/tobs`

#   * Return a JSON list of Temperature Observations (tobs) for the previous year.

# * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

# ## Hints

# * You will need to join the station and measurement tables for some of the analysis queries.

# * Use Flask `jsonify` to convert your API data into a valid JSON response object.



# OPTIONAL IN README HW DIRECTIONS
# # Write a function called `calc_temps` that will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
print(calc_temps('2012-02-28', '2012-03-05'))

# OPTIONAL IN README HW DIRECTIONS Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax 
# for your trip using the previous year's data for those same dates.
# OPTIONAL IN README HW DIRECTIONS
# Plot the results from your previous query as a bar chart. 
# Use "Trip Avg Temp" as your Title
# Use the average temperature for the y value
# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)
# OPTIONAL IN README HW DIRECTIONS 
# Calculate the rainfall per weather station for your trip dates using the previous year's matching dates.
# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation
# OPTIONAL IN README HW DIRECTIONS 
# Create a query that will calculate the daily normals 
# (i.e. the averages for tmin, tmax, and tavg for all historic data matching a specific month and day)
def daily_normals(date):
    """Daily Normals.
    
    Args:
        date (str): A date string in the format '%m-%d'
        
    Returns:
        A list of tuples containing the daily normals, tmin, tavg, and tmax
    
    """
    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    return session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) == date).all()
    
daily_normals("01-01")
# OPTIONAL IN README HW DIRECTIONS 
# calculate the daily normals for your trip
# push each tuple of calculations into a list called `normals`
# Set the start and end date of the trip
# Use the start and end date to create a range of dates
# Stip off the year and save a list of %m-%d strings
# Loop through the list of %m-%d strings and calculate the normals for each date
# OPTIONAL IN README HW DIRECTIONS 
# Load the previous query results into a Pandas DataFrame and add the `trip_dates` range as the `date` index
# OPTIONAL IN README HW DIRECTIONS 
# Plot the daily normals as an area plot with `stacked=False`
