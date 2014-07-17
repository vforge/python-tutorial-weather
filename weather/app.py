"""This is the main app."""


import flask
from .utils import geocode, get_weather_data
from .exceptions import WeatherError


app = flask.Flask(__name__)  # __name__ -> current module name


@app.route('/')
def index():
    """The main index."""
    query = flask.request.args.get('q', '')
    geocode_data = None
    weather_data = None
    error = None

    try:
        if query:
            geocode_data = geocode(query)
            if not geocode_data:
                raise WeatherError('No locations found.')
            weather_data = get_weather_data(geocode_data['lat'],
                                            geocode_data['lon'])
    except WeatherError as ex:
        error = str(ex)
        # error = ex.message

    return flask.render_template(
        'index.html',
        query=query,
        geocode_data=geocode_data,
        weather_data=weather_data,
        error=error,
    )


def run():
    """Run the app"""
    app.debug = True
    app.run()

# if run directly:
# if __name__ == '__main__':
    # running as non-module app.run()
