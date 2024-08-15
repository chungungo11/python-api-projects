# Importing geopy library and Nominatim class
from geopy.geocoders import Nominatim
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry


def get_coordinates():
    # Calling the Nominatim tool and create Nominatim class
    geolocator = Nominatim(user_agent="weather-app")

    # Prompt for location name
    location = input("Enter the name of your location: ")
    # Get location
    get_location = geolocator.geocode(location)
    # Get address
    address = get_location.address
    print("Associated address:\n", address)

    # Get latitude
    latitude = get_location.latitude
    # Get longitude
    longitude = get_location.longitude

    get_weather(latitude, longitude)


def get_weather(latitude, longitude):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m", "precipitation_probability", "precipitation"],
        "timezone": "Europe/Berlin"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_precipitation_probability = hourly.Variables(1).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(2).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["precipitation_probability"] = hourly_precipitation_probability
    hourly_data["precipitation"] = hourly_precipitation

    hourly_dataframe = pd.DataFrame(data = hourly_data)
    print(hourly_dataframe)


if __name__ == "__main__":
    get_coordinates()