import threading
import unittest
from random import random,uniform,randint
from weather.database.AirportDatabaseReader import extractCities
from weather.database.AirportDatabaseReader import readDatabase
from weather.webservice.OpenWeather import verifyCity

def cityName():
	"""
	Crea un nombre de una ciudad hipotetica con 3 Letras mayusculas
	:return city: nombre de ciudad formado por 3 letras mayusculas.
	"""
	city = ""
	for i in range(3):
		letter = random() * 90
		while letter < 65:
			letter = random() * 90
		city += str(chr(int(letter)))
	return city

def path():
	"""
	Devuelve una ruta relativa hipotetica de un sistema de archivos.
	:return path: ruta hipotetica de un sistema de archivos.
	"""
	path = ""
	for i in range(randint(2,100)):
		if randint(0,1) == 0:
			path += "../"
		directory = ""
		for j in range(34):
			directory += str(chr(randint(65,127)))
		path += directory + "/"
	return path

class test_Weather(unittest.TestCase):

	def test_extractCities(self):
		"""
		Prueba la funcion extractCities() de la clase AirportDatabaseReader.
	   	el metodo test_extractCities() prueba al metodo extractCities(), pasandole los argumentos en el formato que deberia ir,
	   	y comprueba que cada parametro en el conjunto devuelto, y pasandole los argumentos en un formato incorrecto, y para 
	   	mostrar la robustez del metodo.

	   	:param self: objeto unittest	
		"""
		database = []
		for i in range(int(random()*10000)):
			database.append("{},{},{},{},{},{}".format(cityName(),cityName(),uniform(-180,180),uniform(-180,180),uniform(-180,180),uniform(-180,180)))
		cities = extractCities(database)

		for city in cities:
			for l in city[0]:
				if ord(l) > 90 or ord(l) < 65:
					raise AssertionError()
			try:
				float(city[1])
				float(city[2])
			except ValueError:
				raise AssertionError()

		database = []
		for i in range(int(random()*10000)):
			database.append("{}{}{}{}{}{}".format(cityName(),cityName(),uniform(-180,180),uniform(-180,180),uniform(-180,180),uniform(-180,180)))
		cities = extractCities(database)
		self.assertEqual(len(cities),0)

	def test_ReadDatabase(self):
		for i in range(randint(0,1000)):
			if path() != "../data/dataset.csv":
				self.assertEqual(readDatabase(path),[])
			else:
				self.assertNotEqual(readDatabase(path),[])

	def test_peticion(self):
		"""
		El metodo test_peticion prueba la funcion verifyCity() del modulo Openweather, el metodo verifyCity, nunca debe mandar una
		excepcion siempre regresa el resultado de la peticion, aun que no pueda realizar bien la solicitud al webservice.
		:param self:
		"""
		database = []
		for i in range(int(random()*100)):
			database.append("{},{},{},{},{},{}".format(cityName(),cityName(),uniform(-180,180),uniform(-180,180),uniform(-180,180),uniform(-180,180)))
		cities = extractCities(database)

		try:
			for city in cities:
				thread = threading.Thread(target=verifyCity,args=(city,))
				thread.start()
		except:
			raise AssertionError()
					
		cities = extractCities(readDatabase("../data/dataset.csv"))

		try:
			for city in cities:
				thread = threading.Thread(target=verifyCity,args=(city,))
				thread.start()
		except:
			raise AssertionError()

if __name__ == '__main__':
	unittest.main()