from setuptools import setup
from weather import __version__


with open('README.rst', 'r') as f:
    # automatically calls 'open' and 'close' methods - we can add those to any class
    long_description = f.read()

setup(
    name='weather',
    version=__version__,
    description='A web app that gets the current weather.',
    long_description=long_description,
    url='http://example.com',
    author='V.',
    author_email='v@wikia-inc.com',
    packages=[
        'weather'
    ],
    install_requires=[
        'Flask==0.10.1',
        'requests==2.3.0',

    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'weather-server=weather.app:run'
        ],
    },
    # packages=find_packages()
)