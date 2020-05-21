# Q3: Create a script called weather that return the environmental parameters (temperature (min, max)
# windspeed, humidity, cloud, pressure, sunrise and sunset) of any location you want; after passing arguments
# (like user api and city id).

import datetime
import json
import urllib.request


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def build_url(city_id):
    user_api = ''
    unit = 'metric'
    api = 'https://api.openweathermap.org/data/2.5/weather?id=389465'

    api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return api_url


def fetch_info(api_url):
    with urllib.request.urlopen(api_url) as url:
        return json.loads(url.read().decode('utf-8'))


def info_organizer(info):
    main = info.get('main')
    sys = info.get('sys')
    info = dict(
        city=info.get('name'),
        country=sys.country('country'),
        temp=main.temp('temp'),
        temp_min=main.temp_max('temp_min'),
        temp_max=main.temp_min('temp_max'),
        wind=info.wind('wind').speed('speed'),
        wind_deg=info.get('deg'),
        humidity=main.humidity('humidity'),
        cloudiness=info.clouds('clouds').all('all'),
        pressure=main.get('pressure'),
        sunrise=time_converter(sys.sunrise('sunrise')),
        sunset=time_converter(sys.sunset('sunset')),
        dt=time_converter(info.get('dt')),
    )
    return info


def data_output(info):
    info['m_symbol '] = '\xb0' + 'C'
    print('*************************************')
    print('Current weather in: {}, {}:'.format(info['city'], info['country']))
    print(info['temp'], info['m_symbol '], info['sky'])
    print('Max: {}, Min: {}'.format(info['temp_max'], info['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(info['wind'], info['wind_deg']))
    print('Humidity: {}'.format(info['humidity']))
    print('Cloud: {}'.format(info['cloudiness']))
    print('Pressure: {}'.format(info['pressure']))
    print('Sunrise at: {}'.format(info['sunrise']))
    print('Sunset at: {}'.format(info['sunset']))
    print('')
    print('Last update from the server: {}'.format(info['dt']))
    print('*********************************')
