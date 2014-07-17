"""Exceptions for Weather."""


class WeatherError(Exception):
    """Base exception for Weather."""
    pass


class OpenStreetMapError(WeatherError):
    """Raised when OpenStreetMap error occurs."""
    pass


class OpenWeatherMapError(WeatherError):
    """Raised when OpenWeatherMap error occurs."""
    pass
