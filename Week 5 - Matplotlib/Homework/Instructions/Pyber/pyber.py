
#Three Observations
#1) There are more drivers in urban areas than in rural and suburban areas, by a large amount
#2) There are more rides in urban areas than in rural and suburban areas, but at a lower proportion than the driver mismatch
#3) The trend continues when looking at fares - overall, this implies that a large number of drivers are competing
#for lower fares per ride in urban areas, relative to rural and suburban areas.

# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"

# Read the City and Ride Data
file1=pd.read_csv(city_data_to_load)
file2=pd.read_csv(ride_data_to_load)

# Combine the data into a single dataset
data_complete = pd.merge(file1, file2, how="left", on=["city", "city"])

# Display the data table for preview
data_complete.head()

#Count rides by city and add column
rides_by_city=data_complete.groupby("city")["ride_id"].count()
rides_by_city=pd.DataFrame(data=rides_by_city)
data_complete = pd.merge(data_complete, rides_by_city,how="left", on=["city", "city"])


#Calc average fare by city and add column
fare_by_city=data_complete.groupby("city")["fare"].mean()
fare_by_city=pd.DataFrame(data=fare_by_city)
data_complete = pd.merge(data_complete, fare_by_city,how="left", on=["city", "city"])
data_complete.tail()

#Format and edit table
data_complete = data_complete.rename(columns={"city":"City",
                                      "type":"Region Type",
                                      "driver_count":"# of Drivers by City",
                                      "fare_x":"Ride Fare",
                                      "fare_y":"Avg Fare in City",
                                      "ride_id_y":"Rides by City"})

del data_complete["date"]
del data_complete["ride_id_x"]

data_complete.tail()



colors=["gold", "lightskyblue", "lightcoral"]
x=data_complete["Rides by City"]
y=data_complete["Avg Fare in City"]
area=data_complete["# of Drivers by City"]
plt.scatter(x, y, s=area, facecolors=colors, alpha=0.1,edgecolors="black")
plt.xlabel("# of Rides Per City")
plt.ylabel("Average Fare")
plt.legend(loc="upper right")
plt.title("Fares, Rides, Drivers, and City Types, Oh My!")
plt.text(2,20,"Size= # drivers")
# plt.show()

# need to get key and colors to align with city type - maybe build plots separately first? didn't figure this out in time

## Bubble Plot of Ride Sharing Data

# Gather data for fares by city type
fares_by_region=data_complete.groupby("Region Type").sum()
fares_by_region=pd.DataFrame(data=fares_by_region)
print(fares_by_region.head())
# (urban=$39,854.38;rural=$4,327.93; suburban=$19,356.33)


# Gather data for ride counts
rides_by_region=data_complete.groupby("Region Type").count()
rides_by_region=pd.DataFrame(data=rides_by_region)
print(rides_by_region.head())
# (urban=1625; rural=125; suburban=625)

# Gather data for total drivers by city type
# drivers_by_region=data_complete.groupby("Region Type").
# drivers_by_region=pd.DataFrame(data=drivers_by_region)

#print(drivers_by_region.head())
# (urban=59602; rural=537; suburban=8570)

#Plot rides by city
labels=["Rural","Suburban","Urban"]

# The values of each section of the pie chart
rides=[125,625,1625]

# The colors of each section of the pie chart
colors = ["gold", "lightcoral", "lightskyblue"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.1)

# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart

plt.pie(rides, explode=explode, labels=labels, colors=colors,
         autopct="%1.1f%%", shadow=True, startangle=140)



plt.title("Rides by City Type")
plt.axis("equal")
plt.savefig("../Rides by City Pie.png")
plt.show()


## Total Fares by City Type

#Plot fares by city
labels=["Rural","Suburban","Urban"]

# The values of each section of the pie chart
fares=[4327.93,19356.33,39854.38]
# (urban=$39,854.38;rural=$4,327.93; suburban=$19,356.33)


# The colors of each section of the pie chart
colors = ["gold", "lightcoral", "lightskyblue"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.1)

# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart

plt.pie(fares, explode=explode, labels=labels, colors=colors,
         autopct="%1.1f%%", shadow=True, startangle=140)

plt.title("Fares by City Type")
plt.axis("equal")
plt.savefig("../Fares by City Pie.png")
plt.show()

# Show Figure
plt.show()

del data_complete["Ride Fare"]
# del data_complete["ride_id_x"]



driver_data=data_complete.drop_duplicates()
driver_data.tail()

# Gather data for driver counts
drivers_by_region=driver_data.groupby("Region Type").sum()
drivers_by_region=pd.DataFrame(data=drivers_by_region)
print(drivers_by_region.head())
# (urban=2405; rural=78; suburban=490)

#Plot drivers by city
labels=["Rural","Suburban","Urban"]

# The values of each section of the pie chart
drivers=[78,490,2405]
# (urban=2405; rural=78; suburban=490)

# The colors of each section of the pie chart
colors = ["gold", "lightcoral", "lightskyblue"]

# Tells matplotlib to seperate the "Python" section from the others
explode = (0, 0, 0.1)

# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart

plt.pie(drivers, explode=explode, labels=labels, colors=colors,
         autopct="%1.1f%%", shadow=True, startangle=170)

plt.title("Drivers by City Type")
plt.axis("equal")
plt.savefig("../Drivers by City Pie.png")
plt.show()