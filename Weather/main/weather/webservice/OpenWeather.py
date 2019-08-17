import requests
from requests.exceptions import ConnectionError
from time import time

def verifyCity(city):
	url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&uk&APPID=9ee969687e25812a1e19a77054ab4003&units=metric".format(city[1], city[2])
	try:
		reponse = requests.get(url)
		weather = reponse.json()["main"]
		location = "Cuidad: {}, lat: {}, lon: {} \n".format(city[0],city[1],city[2])
		location += "Temperatura: {}\n".format(weather["temp"])
		location += "Presion: {}\n".format(weather["pressure"])
		location += "humedad: {}\n".format(weather["humidity"])
		return location
	except KeyError:
		location = "Cuidad: {}, lat: {}, lon: {} \n".format(city[0],city[1],city[2])
		location += "Temperatura: Error en coordenas"
		location += "Presion: Error en coordenas"
		location += "humedad: Error en coordenas"
		return location
	except ConnectionError:
		location = "Cuidad: {}, lat: {}, lon: {} \n".format(city[0],city[1],city[2])
		location += "Temperatura: Error en conexion\n"
		location += "Presion: Error en conexion\n"
		location += "humedad: Error en conexions\n"
		return location
	except:
		location = "Cuidad: {}, lat: {}, lon: {} \n".format(city[0],city[1],city[2])
		location += "Temperatura: Error webservice\n"
		location += "Presion: Error webservice\n"
		location += "humedad: Error webservice\n"
		return location
	finally:
		print(location)