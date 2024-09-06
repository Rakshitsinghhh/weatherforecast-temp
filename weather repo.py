import http.client
import json

# Set up the connection
conn = http.client.HTTPSConnection("yahoo-weather5.p.rapidapi.com")

headers = {
    'x-rapidapi-key': " your api ",  # Replace with your actual RapidAPI key
    'x-rapidapi-host': "  provider"
}

# Send the request
city = input("Enter the city name: ")
conn.request("GET", f"/weather?location={city}&format=json&u=c", headers=headers)
res = conn.getresponse()
data = res.read()

# Decode and parse the JSON data
weather_data = json.loads(data.decode("utf-8"))

# Extracting specific sections of the weather data
location = weather_data.get("location", {})
current_observation = weather_data.get("current_observation", {})
forecasts = weather_data.get("forecasts", [])

# Formatting and displaying the data
print(f"Location: {location.get('city')}, {location.get('country')}")
print(f"Coordinates: {location.get('lat')}, {location.get('long')}")
print(f"Timezone: {location.get('timezone_id')}\n")

# Current observation details
print("Current Weather:")
print(f"  Temperature: {current_observation.get('condition', {}).get('temperature')}°C")
print(f"  Weather: {current_observation.get('condition', {}).get('text')}")
print(f"  Wind: {current_observation.get('wind', {}).get('speed')} km/h, {current_observation.get('wind', {}).get('direction')}")
print(f"  Humidity: {current_observation.get('atmosphere', {}).get('humidity')}%")
print(f"  Pressure: {current_observation.get('atmosphere', {}).get('pressure')} mb")
print(f"  Visibility: {current_observation.get('atmosphere', {}).get('visibility')} km")
print(f"  Sunrise: {current_observation.get('astronomy', {}).get('sunrise')}")
print(f"  Sunset: {current_observation.get('astronomy', {}).get('sunset')}\n")

# Forecast details
print("Forecast:")
for forecast in forecasts:
    print(f"  {forecast.get('day')}: {forecast.get('text')}")
    print(f"    High: {forecast.get('high')}°C, Low: {forecast.get('low')}°C")
conn.close()
