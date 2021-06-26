import requests
api='298c5dc93064a6f65f2124f2aec08b6f'
location=input("enter location(city name):")
API_link="api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api
Report=requests.get(API_link)
About=Report.json()
temperature=((About['main']['temp'])-273.15)
weather=About['weather'][0]['description']
humidity=About['main']['humidity']
windspeed=About['wind']['speed']
with open('weather.txt','w') as f:
    f.write(temperature)
    f.write(weather)
    f.write(humidity)
    f.write(windspeed)

