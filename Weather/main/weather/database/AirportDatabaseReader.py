def readDatabase(path):
	database = open(path)
	cities = database.read().splitlines()[1:]
	database.close()
	return cities
	
def extractCities(database,cities):
	for row in database:
		parameters = row.split(",")
		cities[(parameters[0],parameters[2],parameters[3])] = None
		cities[(parameters[1],parameters[4],parameters[5])] = None