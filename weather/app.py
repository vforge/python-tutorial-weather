"""This is the main app."""

import flask
from .utils import geocode


app = flask.Flask(__name__) # __name__ -> current module name


@app.route('/')
def index():
    query = flask.request.args.get('q', '')
    geocode_data = None

    if query:
        geocode_data = geocode(query)

    return flask.render_template(
        'index.html',
        query=query,
        geocode_data=geocode_data
    )

def run():
    """Run the app"""
    app.debug = True
    app.run()

# if run directly:
# if __name__ == '__main__':
    # running as non-module app.run()