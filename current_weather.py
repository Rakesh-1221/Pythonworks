import requests
from pprint import pprint

api_key="c144faf88706d51e332d386aa443f090"
base_url="http://api.openweathermap.org/data/2.5/weather?"

city_name=input("Enter the city name:")
final_url=base_url + "appid=" + api_key + "&q=" + city_name
weather_data=requests.get(final_url).json()

temp=weather_data['main']['temp']
wind_speed=weather_data['wind']['speed']
description=weather_data['weather'][0]['description']
latitude = weather_data['coord']['lat']
longitude = weather_data['coord']['lon']

print("tempreture",temp)
print("Wind",wind_speed)
print("Description",description)
print("latitude",latitude)
print("longitude",longitude)
