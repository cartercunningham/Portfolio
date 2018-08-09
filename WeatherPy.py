
# Observation 1: At the time and for the city-set I reviewed, there is a clear pattern that temperature tends to increase as the latitude approaches 0 (from either side). 
# Observation 2: That said, temperature clusters are similar for latitudes of -20 to 40, then begin to bend down, creating an "arch" shape overall.
# Observation 3: Wind, humidity, and cloud levels do not appear to have a clear relationship with latitude.


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

# Import API key
from api_keys import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

## Generate Cities List
# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print(len(cities))

## Perform API Calls

# OpenWeatherMap API Key
# Create dataframe using cities list
cities_df=pd.DataFrame(data=cities)

# set up additional columns to hold information
cities_df['Cloudiness'] = ""
cities_df['Country'] = ""
cities_df['Lat'] = ""
cities_df['Lon'] = ""
cities_df['Temp'] = ""
cities_df['Wind'] = ""
cities_df["Humidity"]=""

# Rename first column to "City" and check column headers
cities_df.columns=["City","Cloudiness", "Country","Lat","Lon","Temp","Wind","Humidity"]
cities_df.head()


# create a params dict that will be updated with new city each iteration
params = {"APPID": api_key}

# Loop through the cities_df and find values of interest for each city
for index, row in cities_df.iterrows():
    base_url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial"

    city = row['City']

    # update address key value
    params['q'] = city

    # make request
    cities_weather = requests.get(base_url, params=params)
    
    # print the cities_weather url, avoid doing for public github repos in order to avoid exposing key
    print(f"Accessing data for {city}. URL: ")
    print(cities_weather.url)
    
    
    # convert to json
    cities_weather = cities_weather.json()
    
    # write 
    try:
        cities_df.loc[index, "Lat"] = cities_weather["coord"]["lat"]
        cities_df.loc[index, "Lon"] = cities_weather["coord"]["lon"]
        cities_df.loc[index, "Cloudiness"] = cities_weather["clouds"]["all"]
        cities_df.loc[index, "Wind"] = cities_weather["wind"]["speed"]
        cities_df.loc[index, "Temp"] = cities_weather["main"]["temp"]
        cities_df.loc[index, "Country"] = cities_weather["sys"]["country"]
        cities_df.loc[index, "Humidity"] = cities_weather["main"]["humidity"]

    except:
        print("Missing field/result...skipping.")

# Visualize to confirm lat lng appear
cities_df.head()

# remove rows with no data
cities_df_clean=cities_df[cities_df.Lat.values.astype(bool)]

# Reset datatypes for numeric columns
cities_df_clean[['Cloudiness',"Lat","Lon","Temp","Wind"]] = cities_df_clean[['Cloudiness',"Lat","Lon","Temp","Wind"]].apply(pd.to_numeric)

# Create 4 plots and save csv
x_data=cities_df_clean["Lat"]
temp_data=cities_df_clean["Temp"]


plt.scatter(x=x_data,y=temp_data)
plt.xlabel("Latitude")
plt.ylabel("Temperature")
plt.title("Temperature vs. Latitudes (8/9/18)")
# xmin, xmax = xlim()  # return the current xlim
# xlim((-90, 90))   # set the xlim to xmin, xmax
plt.xlim([-90, 90])
plt.grid(alpha=0.75)

# Save png file
plt.savefig("../TempChart.png")

x_data=cities_df_clean["Lat"]
hum_data=cities_df_clean["Humidity"]


plt.scatter(x=x_data,y=hum_data)
plt.xlabel("Latitude")
plt.ylabel("Humidity")
plt.title("Humidity vs. Latitudes (8/9/18)")
# xmin, xmax = xlim()  # return the current xlim
# xlim((-90, 90))   # set the xlim to xmin, xmax
plt.xlim([-90, 90])
plt.grid(alpha=0.75)

# Save png file
plt.savefig("../HumidityChart.png")

x_data=cities_df_clean["Lat"]
cloud_data=cities_df_clean["Cloudiness"]


plt.scatter(x=x_data,y=cloud_data)
plt.xlabel("Latitude")
plt.ylabel("Cloudiness")
plt.title("Cloudiness vs. Latitudes (8/9/18)")
# xmin, xmax = xlim()  # return the current xlim
# xlim((-90, 90))   # set the xlim to xmin, xmax
plt.xlim([-90, 90])
plt.grid(alpha=0.75)

# Save png file
plt.savefig("../CloudinessChart.png")

x_data=cities_df_clean["Lat"]
wind_data=cities_df_clean["Wind"]


plt.scatter(x=x_data,y=wind_data)
plt.xlabel("Latitude")
plt.ylabel("Wind")
plt.title("Wind vs. Latitudes (8/9/18)")
# xmin, xmax = xlim()  # return the current xlim
# xlim((-90, 90))   # set the xlim to xmin, xmax
plt.xlim([-90, 90])
plt.grid(alpha=0.75)

# Save png file
plt.savefig("../WindChart.png")

# Save cities csv
cities_df_clean.to_csv("../cities weather.csv", encoding='utf-8', index=False)