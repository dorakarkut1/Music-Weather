from CurrentWeather import current_weather
from Get_location import get_location
import datetime

def get_time():
    now_date = datetime.datetime.now()
    hour = int('{:02d}'.format(now_date.hour))
    minute = '{:02d}'.format(now_date.minute)
    hour += int(minute)/100
    return hour

def decision_maker():
    (current_temperature, current_pressure, current_humidity, weather_description, weather_description_id,sunrise,sunset) = current_weather(get_location())
    hour = get_time()
 
    if (hour > sunset or hour < sunrise) and weather_description_id in [800,801]:
        return "campfire.mp4"
    elif (hour > sunset or hour < sunrise) and weather_description_id not in [800,801]:
        return "rain.mp4"
    else:
        if weather_description_id in range(200,299):
            return "thunderstorm.mp4"
        elif weather_description_id in [800,801]:
            return "spring.mp4"
        elif weather_description_id in range(802,899):
            return "wind.mp4"
        elif weather_description_id in range(600,699):
            return "snow.mp4"
        elif weather_description_id in range(300,399) or weather_description_id in range(500,599):
            return "rain.mp4"
if __name__ == '__main__':
    decision_maker()
