import requests
api_key = "9718f7369339358e77af1a80d911104a"
city_name = input("Enter a city name: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response = requests.get(weather_url)
weather_info = response.json()
temp=round(response.json()['main']['temp'])
print(response.status_code)
print(f"The weather in {city_name} : {weather_info}")
print(f"The teamperature in {city_name} : {temp} F")

