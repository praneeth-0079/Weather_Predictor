import requests
api = '298c5dc93064a6f65f2124f2aec08b6f'
location = input("enter location(city name):")
API_link = "api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api
Report = requests.get(API_link)
About = Report.json()
tempe = ((About['main']['temp'])-273.15)
Wthr = About['weather'][0]['description']
Hmd = About['main']['humidity']
WS = About['wind']['speed']
with open('weather.txt','w') as f:
    f.write("temperature in deg C:")
    f.write(tempe)
    f.write("weather:")
    f.write(Wthr)
    f.write("Humidity in %:")
    f.write(Hmd)
    f.write("wind speed in KMPH:")
    f.write(WS)

