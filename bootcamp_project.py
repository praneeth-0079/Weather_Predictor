import requests
api='298c5dc93064a6f65f2124f2aec08b6f'
location=input("enter location(city name):")
URL="api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api
link=requests.get(URL)
data=link.json()
temperature=((data['main']['temp'])-273.15)
weather=data['weather'][0]['description']
humidity=data['main']['humidity']
windspeed=data=['wind']['speed']
with open('weather.txt','w') as f:
    f.write(temperature)
    f.write(weather)
    f.write(humidity)
    f.write(windspeed)

