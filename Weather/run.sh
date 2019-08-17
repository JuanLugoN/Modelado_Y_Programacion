#!/bin/bash
pip install requests
cd main/
python setup.py sdist
cd dist 
pip install weather-0.1.tar.gz
cd ../weather/
reset
python WeatherOfLocations.py