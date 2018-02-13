# opsdroid weather skill 

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to tell you the current weather by zip code

## Requirements 

You need an API Key from [OpenWeatherMap](https://openweathermap.org/api).

## Configuration

In `configuration.yaml`, set up the following: 

    skills:
        - name: weather
          zip: 66044,US     # Zip,Country Code
          units: imperial   # metric is also an option
          api-key: abcdefg  # Your API key, not in quotes 

## Usage 

Opsdroid will tell you the current weather conditions (temperature and humidity level), and will inject some commentary. 

> User: How's the weather? 

> opsdroid: Not too bad! It's currently 45 and 34% humidity in Lawrence.

## Resources 

- opsdroid [official weather skill](https://github.com/opsdroid/skill-weather)
- opsdroid [weather skill tutorial](https://opsdroid.readthedocs.io/en/stable/tutorials/create-weather-skill/)
- [opsdroid docs](https://opsdroid.readthedocs.io/)