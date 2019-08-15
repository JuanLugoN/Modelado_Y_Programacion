import requests

def verifyCity(city)
	url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&uk&APPID=9ee969687e25812a1e19a77054ab4003".format(city[1], city[2])
	try:
		reponse = requests.get(url)
		weather = reponse.json()["main"]
	except KeyError:
		return False
	return 

