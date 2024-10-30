import requests
import json

API_key = "a98af8f99f29dc71e9874944f5815699"
city = input("Give city: ")

url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_key}"
response = requests.get(url)
data = response.json()

lat = data[0]["lat"]
lon = data[0]["lon"]

weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
current_weather = requests.get(weather_url).json()

temperature = current_weather["main"]["temp"]
description = current_weather["weather"][0]["description"]

print(f"Sää kaupungissa {city}:")
print(f"Lämpötila: {temperature} °C")
print(f"Säätila: {description.capitalize()}")