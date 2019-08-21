def readDatabase(path):
	"""
	Lee una base de datos a partir de la su ruta absoluta o relativa, devuelve una lista, con las lineas leidas
	en la base de datos.

	:param path: ruta absula o relativa de la base de datos.
	:return cities: una lista con ciudades no ordenadas por elementos en la lista.
	"""
	try:
		database = open(path)
		cities = database.read().splitlines()[1:]
		database.close()
		return cities
	except:
		cities = []
		return cities
	
def extractCities(database):
	"""
	Dada una lista donde cada elemento = origin,destination,origin_latitude,origin_longitude,destination_latitude,destination_longitude
	extrae extrae las ciudades de cada elemento en la lista, y los agrega a un diccionario, donde la llave, es una tupla, con los parametros
	yamencionados, si los elementos no se encuentran de la forma antes mencionada el metodo regresa un diccacioionario vacio

	:param database: Lista con ciudades no ordenadas por elementos en la lista.
	:param cities: diccionario de paises
	"""
	cities = {}
	try:
		for row in database:
			parameters = row.split(",")
			cities[(parameters[0],parameters[2],parameters[3])] = None
			cities[(parameters[1],parameters[4],parameters[5])] = None
		return cities
	except:
		cities = {}
		return cities