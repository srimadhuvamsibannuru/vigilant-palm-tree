import os 
import requests as re


def get_weather_data(location,apikey):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}&units=metric'
    response = re.get(url)
    if response.status_code == 200:
        c = response.json()
        weather = c['main']['temp']
        feels_like = c['main']['feels_like']
        min_temp = c['main']['temp_min']
        max_temp = c['main']['temp_max']
        location = c['name']
    else:
        print('issue in API')
    return {'weather':weather,'feels_like':feels_like,'min_temp':min_temp,'max_temp':max_temp,'location':location}




    
    




    

