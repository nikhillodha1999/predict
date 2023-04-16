import requests

# Set the API endpoint and parameters
url = 'https://api.openweathermap.org/data/2.5/weather'
city = 'Buxar'  # Replace with the city name you want to fetch data for
api_key = '2129dff76f701a1fdd061266ba34a79b'  # Replace with your OpenWeatherMap API key
params = {
    'q': city,
    'units': 'metric',
    'appid': api_key
}

# Send request to the API
response = requests.get(url, params=params)

# Check if the response was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    rainfall = data.get('rain', {}).get('1h', 0)
    print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Rainfall: {rainfall}mm")
else:
    print(f"Failed to fetch weather data for {city}. Status code: {response.status_code}")
