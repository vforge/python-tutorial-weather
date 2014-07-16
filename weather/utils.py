"""Utility functions for Weather."""


import requests

from .exceptions import GeocodeError


def geocode(query):
    """Geocode location using OpenStreetMap."""
    response = requests.get(
        'http://nominatim.openstreetmap.org/search',
        params={'q': query, 'format': 'json'},
    )

    if response.status_code != 200:
        raise GeocodeError('Got non-ok status from OpenStreetMap')

    data = response.json()

    return data


