from opsdroid.matchers import match_regex

import aiohttp


async def get_weather(config):
    api_url = "http://api.openweathermap.org/data/2.5/weather?"
    parameters = "zip={}&units={}&appid={}".format(
        config['zip'], config['units'], config['api-key'])

    async with aiohttp.ClientSession() as session:
        response = await session.get(api_url + parameters)
    return await response.json()


@match_regex(r"(H?h?ow\'?s the weather\??)")
async def tell_weather(opsdroid, config, message):
    weather_data = await get_weather(config)
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    city = weather_data['name']

    if temp < 40:
        msg = "It's freaking cold!"
    elif temp > 85:
        msg = "It's like the surface of the sun!"
    else:
        msg = "Not too bad!"

    await message.respond("{} It's {} and {}% humidity in {}.".format(msg, int(temp), humidity, city))
