from weather.database.AirportDatabaseReader import extractCities
from weather.database.AirportDatabaseReader import readDatabase
from weather.webservice.OpenWeather import verifyCity
import threading
import time
"""
Modulo principal, de una aplicacion que lee la base de datos de un aeropuerto muestra el clima de las ciudades de origen
y de llegada, obteniendo el clima de una werbservice.
"""
if __name__ == '__main__':
	"""
	Metodo Principal del modulo.
	"""
	data = "../../data/dataset.csv"
	flights = readDatabase(data)
	cities = extractCities(flights)
	for city in cities:
		cities[city] = verifyCity(city)

	for flight in flights:
		parameters = flight.split(",")
		print("___________________________________________________________________________")
		print("Origen : " + cities[(parameters[0],parameters[2],parameters[3])])
		print("Destiono: " + cities[(parameters[1],parameters[4],parameters[5])])
		print("---------------------------------------------------------------------------")
