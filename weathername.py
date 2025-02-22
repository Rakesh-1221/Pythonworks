import requests
from pprint import pprint

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "c144faf88706d51e332d386aa443f090"
city_name = input("Enter the name")
final_url = base_url + "appid=" + api_key + "&q=" + city_name
weather_data = requests.get(final_url).json()
pprint(weather_data)
print("URL",final_url)