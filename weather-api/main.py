import json
import math
import os

from dotenv import load_dotenv, find_dotenv
import requests
from typing import Any

try:
    from mappers import weather_api_mapping
except ModuleNotFoundError:
    from .mappers import weather_api_mapping

load_dotenv(find_dotenv())
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

class UnknownLocationException(Exception):
    ...


class APIError(Exception):
    ...


def get_weather_api_data(location: str) -> dict:
    api_key = WEATHER_API_KEY
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 400:
        raise UnknownLocationException
    if response.status_code != 200:
        raise APIError
    return response.json()

def get_location_from_event(event: dict) -> str:
    # locally the event isn't formatted like production, so pass the event as default
    body_json = event.get("body", event)
    try:
        body = json.loads(body_json)
        location = str(body.get("location"))
    except TypeError:
        location = body_json.get("location")
    return location

def get_weather_location(weather_data: dict) -> str:
    """
    from the data returned by the weather api,
    if the `location.country` is "USA", add the region
      otherwise just return the location.name
    """
    location = weather_data.get("location", {})
    country = location.get("country", "").lower()
    location_name = location.get("name", "")
    if country in ("usa", "united states of america"):
        location_name += f", {location.get('region')}"
    return location_name

def get_weather_condition(weather_data: dict) -> str:
    current_weather = weather_data.get("current", {})
    condition = current_weather.get("condition", {})
    code = condition.get("code")

    return weather_api_mapping[code].value

def get_fahrenheit(weather_data: dict) -> int:
    current_weather = weather_data.get("current", {})
    fahrenheit = current_weather.get("temp_f")

    # rounded this way because floating point format represents binary not decimal
    return int(fahrenheit + math.copysign(0.5, fahrenheit))

def format_weather_payload(weather_data: dict) -> dict:
    return {
        "condition": get_weather_condition(weather_data),
        "location": get_weather_location(weather_data),
        "temperature": get_fahrenheit(weather_data)
    }

def lambda_handler(event: dict, context: Any):
    # qs_params = event.get("queryStringParameters") # dict of key-value pairs
    try:
        location = get_location_from_event(event)
        weather_data = get_weather_api_data(location)
        if not weather_data:
            raise APIError
        status_code = 200
        message = json.dumps(format_weather_payload(weather_data))
    except UnknownLocationException:
        status_code = 400
        message = "Location missing or unknown."
    except APIError:
        status_code = 500
        message = "Error from weather API."

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST",
            "Access-Control-Allow-Credentials": True
        },
        "body": message
    }


if __name__ == "__main__":
    pass
