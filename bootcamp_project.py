import requests
api = '298c5dc93064a6f65f2124f2aec08b6f'
location = input("enter location(city name):")

api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api
link = requests.get(api_link)
api_data = link.json()


temp_city = ((api_data['main']['temp']) - 273)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
with open('weather.txt' , 'w') as f:
    f.write("temperature in deg C:")
    f.write(format(temp_city))
    f.write("; weather:")
    f.write(weather_desc)
    f.write("; Humidity in %:")
    f.write(format(hmdt))
    f.write("; wind speed in KMPH:")
    f.write(format(wind_spd))



