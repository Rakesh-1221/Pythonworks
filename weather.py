import requests
from pprint import pprint

api_key = "c144faf88706d51e332d386aa443f090"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_id = input("Enter the city id:")
final_url = base_url + "appid=" + api_key + "&id=" + city_id
weather_data = requests.get(final_url).json()
pprint(weather_data)
