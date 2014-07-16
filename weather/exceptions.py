"""Exceptions for Weather."""


class WeatherError(Exception):
    """Base exception for Weather."""
    pass


class GeocodeError(WeatherError):
    """Raised when geocode error occurs."""
    pass