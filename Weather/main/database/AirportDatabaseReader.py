def readDatabase(path):
	database = open(path)
	return database.read().splitlines()[1:]

def extractCities(database):
	citiesList = []
	for row in database:
		parameters = row.split(",")
		citiesList.append((parameters[0],parameters[2],parameters[3]))
		citiesList.append((parameters[1],parameters[4],parameters[5]))
	return citiesList