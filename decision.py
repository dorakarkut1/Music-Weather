""" Make decision on video
This script based on current weather decides which video should be played. It can be imported as
module and contains the following functions:

    * get_time - returns current hour
    * decision_maker - returns name of the video that should be played
"""

import datetime
from current_weather import get_current_weather
from get_location import get_location

def get_time():
    """Returns current hour

    Parameters
    ----------
    None

    Returns
    -------
    int
        Current hour.minutes
    """
    now_date = datetime.datetime.now()
    hour = int('{:02d}'.format(now_date.hour))
    minute = '{:02d}'.format(now_date.minute)
    hour += int(minute)/100
    return hour

def decision_maker():
    """returns name of the video that should be played

    Parameters
    ----------
    None

    Returns
    ----------
    str
        name of the video that should be played: name.mp4
    """
    (weather_description_id,sunrise,sunset) = get_current_weather(get_location())
    hour = get_time()

    if (hour > sunset or hour < sunrise) and weather_description_id in [800,801]:
        return "campfire.mp4"
    if (hour > sunset or hour < sunrise) and weather_description_id not in [800,801]:
        return "rain.mp4"
    if weather_description_id in range(200,299):
        return "thunderstorm.mp4"
    if weather_description_id in [800,801]:
        return "spring.mp4"
    if weather_description_id in range(300,399) or weather_description_id in range(802,899):
        return "wind.mp4"
    if weather_description_id in range(600,699):
        return "snow.mp4"
    return "rain.mp4"

if __name__ == '__main__':
    print(decision_maker())
