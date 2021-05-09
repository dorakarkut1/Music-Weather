
import requests, json, pytemperature
import numpy as np
from get_api_number import get_api

def current_weather(city_name,api_key):	
	
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	
	# complete url address
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	response = requests.get(complete_url)
	data = response.json()
	#check if city was found
	if data["cod"] != "404":

		#unpacking dictionary
		y = data["main"]

		current_temperature = np.round(pytemperature.k2c(y["temp"]))
		current_pressure = y["pressure"]
		current_humidity = y["humidity"]
		weather_description = data["weather"][0]["id"]
		sunrise = data["sys"]["sunrise"]
		sunset = data["sys"]["sunset"]

		return (current_temperature, current_pressure, current_humidity, weather_description,sunrise,sunset)
	else:
		return None




if __name__ == '__main__':
	api = get_api("weather")
	print(current_weather("Gdańsk", api))