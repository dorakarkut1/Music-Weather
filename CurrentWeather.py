
import requests, json, pytemperature
import numpy as np


def current_weather(city_name,api_key):	
	
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	
	# complete url address
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	response = requests.get(complete_url)
	x = response.json()
	#check if city was found
	if x["cod"] != "404":

		#unpacking dictionary
		y = x["main"]

		current_temperature = np.round(pytemperature.k2c(y["temp"]))

		current_pressure = y["pressure"]

		current_humidity = y["humidity"]
		#unpacking dictionary
		z = x["weather"]

		weather_description = z[0]["description"]

		return (current_temperature, current_pressure, current_humidity, weather_description)
	else:
		return None


def get_api():
	with open('./api', 'r') as f:
		for line in f:
			if line.startswith("weather"):
				line = line.split()
				api = line[1]
		return api

if __name__ == '__main__':
	api = get_api()
	print(current_weather("Gdańsk", api))