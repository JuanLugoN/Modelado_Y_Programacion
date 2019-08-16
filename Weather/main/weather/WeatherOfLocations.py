from weather.database.AirportDatabaseReader import extractCities
from weather.database.AirportDatabaseReader import readDatabase
from weather.webservice.OpenWeather import verifyCity
#from time import sleep
#from time import time

data = "../../data/dataset.csv"
weatherOfLocations = {}
extractCities(readDatabase(data),weatherOfLocations)
i = 0
for city in weatherOfLocations:
	if weatherOfLocations[city] == None: #or time() - weatherOfLocations[city][1] >= 6000 or ~weatherOfLocations[city][2]:
		weatherOfLocations[city] = verifyCity(city)
		print(weatherOfLocations[city])
		i += 1
print(i)