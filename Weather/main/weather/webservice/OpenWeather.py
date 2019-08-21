import requests
from requests.exceptions import ConnectionError

def verifyCity(city):
	"""
	Dadas la longitud y latitud de una ciudad, regresa el clima de dicha ciudad o lugar en tiempo real.

	:param city: ciudad de la que se quiere conocer el clima.
	:param l:
	"""
	url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&uk&APPID=9ee969687e25812a1e19a77054ab4003&units=metric".format(city[1], city[2])
	try:
		reponse = requests.get(url)
		mainWeather = reponse.json()["main"]
		location = "Ciudad: {}, lat: {}, lon: {} \n".format(city[0],city[1],city[2])
		location += "Temperatura: {}°C\n".format(mainWeather["temp"])
		location += "Presión: {}\n".format(mainWeather["pressure"])
		location += "humedad: {}\n".format(mainWeather["humidity"])
	except KeyError:
		location = "Ciudad: {}, lat: {}, lon: {} \n".format(city[0],city[1],city[2])
		location += "Temperatura: Error en coordenadas\n"
		location += "Presión: Error en coordenadas\n"
		location += "humedad: Error en coordenadas\n"
	except ConnectionError:
		location = "Ciudad: {}, lat: {}, lon: {} \n".format(city[0],city[1],city[2])
		location += "Temperatura: Error en conexión\n"
		location += "Presión: Error en conexión\n"
		location += "humedad: Error en conexión\n"
	except:
		location = "Ciudad: {}, lat: {}, lon: {} \n".format(city[0],city[1],city[2])
		location += "Temperatura: Error webservice\n"
		location += "Presión: Error webservice\n"
		location += "humedad: Error webservice\n"
	finally:
		return location