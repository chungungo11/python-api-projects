# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# calling the Nominatim tool and create Nominatim class
geolocator = Nominatim(user_agent="weather-app")

# entering the location name
get_location = geolocator.geocode("Szigetszentmarton")

# printing address
print(get_location.address)

# printing latitude and longitude
print("Latitude = ", get_location.latitude, "\n")
print("Longitude = ", get_location.longitude)