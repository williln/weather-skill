import aiohttp

from opsdroid.matchers import match_regex

from .constants import CITIES


async def get_weather(config, city=''):
    """
    Can take the name of a city included in CITIES, or can take a US zip code.
    """
    # Check if zip code was passed
    try:
        zip = int(city)
    # Not zip code; see if city in CITIES
    except ValueError:
        try:
            zip = CITIES[city.lower()]
        except KeyError:
            zip = CITIES['lawrence']

    zip = '{},US'.format(zip)

    api_url = "http://api.openweathermap.org/data/2.5/weather?"
    parameters = "zip={}&units={}&appid={}".format(
        zip, config['units'], config['api-key'])

    async with aiohttp.ClientSession() as session:
        response = await session.get(api_url + parameters)
    return await response.json()


# Matches a city name or a 5-digit zip code
@match_regex(r'H?h?ow\'?s the weather in ([a-zA-Z]+(?:[\s-][a-zA-Z]+)*|\d{5})?\??$')
async def tell_weather_city(opsdroid, config, message):
    input_city = message.regex.group(1)
    weather_data = await get_weather(config, city=input_city)
    msg = prepare_message(weather_data)

    await message.respond(msg)


def prepare_message(weather_data):
    try:
        temp = weather_data['main']['temp']
    except KeyError:
        return "Cannot process your weather!"

    try:
        humidity = weather_data['main']['humidity']
    except KeyError:
        return "Cannot process your weather!"

    try:
        city = weather_data['name']
    except KeyError:
        return "Cannot process your weather!"

    if temp < 40:
        msg = "It's freaking cold!"
    elif temp > 85:
        msg = "It's like the surface of the sun!"
    else:
        msg = "Not too bad!"

    message = "{} It's {} and {}% humidity in {}.".format(msg, int(temp), humidity, city)
    return message
