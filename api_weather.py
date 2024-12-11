import os 
import requests as re


location = "Nandyal"
apikey = "e25a7a179d5260a6b68dfc5f7a644c04"
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}&units=metric'
response = re.get(url)
if response.status_code == 200:
    c = response.json()
    weather = c['main']['temp']
    feels_like = c['main']['feels_like']
    min_temp = c['main']['temp_min']
    max_temp = c['main']['temp_max']
    location = c['name']
    
    




    

