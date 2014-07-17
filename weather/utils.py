"""Utility functions for Weather."""


import requests

from .exceptions import OpenStreetMapError, OpenWeatherMapError


def geocode(query):
    """Geocode location using OpenStreetMap."""
    response = requests.get(
        'http://nominatim.openstreetmap.org/search',
        params={'q': query, 'format': 'json'},
    )

    if response.status_code != 200:
        raise OpenStreetMapError('Got non-ok status from OpenStreetMap')

    data = response.json()

    if not data:
        return None

    return data[0]


def get_weather_data(lat, lon):
    """Get current weather for a given lat and lon."""
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather',
        params={'lat': lat, 'lon': lon, 'units': 'metric'}
    )

    if response.status_code != 200:
        raise OpenWeatherMapError('Got non-ok status from OpenWeatherMap')

    data = response.json()

    data['wind']['direction'] = degrees_to_direction(data['wind']['deg'])

    return data


def degrees_to_direction(degrees):
    """Convert degrees to a compass direction."""
    directions = [
        'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
        'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
    ]
    return directions[int(round(float(degrees) / 22.5)) % 16]
