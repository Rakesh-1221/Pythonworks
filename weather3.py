import requests
from pprint import pprint

api_key = "c144faf88706d51e332d386aa443f090"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
latitude = input("Enter Latitude : ")
longitude = input("Enter Longitude : ")
final_url = base_url + "appid=" + api_key + "&lat=" + latitude + "&lon=" + longitude
weather_data = requests.get(final_url).json()
pprint(weather_data)
