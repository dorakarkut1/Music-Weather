"""Current Weather

This script based on location gets and returns current weather: pressure, humidity, weather description, sunrise and sunset time.

This script requires that 'requests', 'json', 'pytemperature', 'time', 'typing' be installed within the Python
environment you are running this script in. It also requires module get_api_number 
from Music_Weather repository.

This file can also be imported as a module and contains the following
functions:

    * timestamp2time - based on timestamp return an hour
	* current_weather - based on location returns current_pressure, current_humidity, weather_description, weather_description_id,sunrise,sunset
"""

import requests, json, pytemperature, typing
import numpy as np
from get_api_number import get_api
import time


def timestamp2time(timestamp):
	"""
	Based on timestamp return an hour

    Parameters
    ----------
    timestamp : int
		timestamp

    Returns
    -------
    int 
        Int which contains an hour 
    """
	hour = time.strftime("%D %H:%M", time.localtime(int(timestamp)))
	return hour

def current_weather(city_name:str) -> tuple:	
	"""
	Based on location returns current_pressure, current_humidity, weather_description, 
	weather_description_id,sunrise,sunset time
    
	Parameters
    ----------
    city_name : str
		String which contains name of the city
	api_key : object
		Object which contains API key necessary to connect to the server

    Returns
    -------
    tuple
		Set of information about weather: current_temperature: int, current_pressure: int, current_humidity: int, 
		weather_description: str, weather_description_id: int, sunrise time: tuple(int,int), sunset time: tuple(int,int)
    """

	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	api_key = get_api("weather")
	# complete url address
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	response = requests.get(complete_url)
	data = response.json()
	#check if city was found
	if data["cod"] != "404":

		#unpacking dictionary
		y = data["main"]

		current_temperature = int(np.round(pytemperature.k2c(y["temp"])))
		current_pressure = int(y["pressure"])
		current_humidity = int(y["humidity"])
		weather_description_id = int(data["weather"][0]["id"])
		weather_description = str(data["weather"][0]["description"])
		sunrise = timestamp2time(data["sys"]["sunrise"]).split()[1].split(":")
		sunrise = [ int(x) for x in sunrise]
		sunset = timestamp2time(data["sys"]["sunset"]).split()[1].split(":")
		sunset = [ int(x) for x in sunset]

		return (current_temperature, current_pressure, current_humidity, weather_description, weather_description_id,sunrise,sunset)
	else:
		return None




if __name__ == '__main__':
	
	print(current_weather("Gdańsk"))