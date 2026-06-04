import requests

city = input("Enter city name: ")

url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

response = requests.get(url)
data = response.json()

if "results" not in data:
    print("City not found.")
    exit()

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]

weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,wind_speed_10m,weather_code"
)

weather_response = requests.get(weather_url)
weather_data = weather_response.json()

current = weather_data["current"]

weather_conditions = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Light Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Light Snow",
    73: "Moderate Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    95: "Thunderstorm"
}

temperature = current["temperature_2m"]
wind_speed = current["wind_speed_10m"]
time= current["time"]
time = time.replace("T", " ")
weather_code = current["weather_code"]
condition = weather_conditions.get(weather_code, "Unknown")

print("\n🌤️ Weather Report")
print(f"📍City: {city}")
print(f"🌡️ Temperature: {round(temperature, 1)} °C")
print(f"💨Wind Speed: {round(wind_speed, 2)} km/h")
print(f"🌫️ Weather Condition:", condition)
print(f"⏱️ Time: {time}")
