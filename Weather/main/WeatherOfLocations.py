# Main Module 

import database.AirportDatabaseReader

isValidDatabase = True
try:
	data = "../data/dataset.csv"
	citiesList = database.AirportDatabaseReader.extractCities(database.AirportDatabaseReader.readDatabase(data))
except IOError:
	isValidDatabase = False

#while isValidDatabase:
for city in citiesList:
	print(city)
