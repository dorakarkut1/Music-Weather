"""Current Weather

This script based on location gets and returns current weather: pressure, humidity,
weather description, sunrise and sunset time.

This script requires that 'requests', 'json', 'pytemperature', 'time', 'typing'
be installed within the Python environment you are running this script in. It
also requires module get_api_number from Music_Weather repository.

This file can also be imported as a module and contains the following
functions:

    * timestamp2time - based on timestamp return an hour
	* current_weather - based on location returns current_pressure,
	current_humidity, weather_description, weather_description_id,sunrise,
	sunset
"""

import time
import requests
import pytemperature
import numpy as np
from get_api_number import get_api



def timestamp_2_time(timestamp):
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
    return time.strftime("%D %H:%M", time.localtime(int(timestamp)))


def get_current_weather(city_name:str) -> tuple:
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
		Set of information about weather: current_temperature: int, current_pressure:
		int, current_humidity: int, weather_description: str, weather_description_id:
		int, sunrise time: int, sunset time: int
    """

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + get_api("weather") + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()

	#if city was found unpacking data
    if data["cod"] != "404":
        all_data = data["main"]
        current_temperature = int(np.round(pytemperature.k2c(all_data["temp"])))
        current_pressure = int(all_data["pressure"])
        current_humidity = int(all_data["humidity"])
        weather_description_id = int(data["weather"][0]["id"])
        weather_description = str(data["weather"][0]["description"])
        sunrise = timestamp_2_time(data["sys"]["sunrise"]).split()[1].split(":")
        sunrise = [ int(x) for x in sunrise]
        sunrise_converted = sunrise[0]+ sunrise[1]/100
        sunset = timestamp_2_time(data["sys"]["sunset"]).split()[1].split(":")
        sunset = [ int(x) for x in sunset]
        sunset_converted = sunset[0]+ sunset[1]/100
        return (current_temperature, current_pressure, current_humidity, weather_description,
                weather_description_id,sunrise_converted,sunset_converted)
    return None


if __name__ == '__main__':

    print(get_current_weather("Gdańsk"))
