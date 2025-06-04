import requests

API_KEY = "73f15c2930eff02a84a0bc2a17e9e673"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            raise Exception(data.get("message", "Error fetching weather"))

        return {
            "condition": data["weather"][0]["main"],
            "temp": data["main"]["temp"]
        }
    except Exception as e:
        print(f"⚠️ Error getting weather for {city}: {e}")
        return {
            "condition": "Unknown",
            "temp": 25  # Default temperature if API call fails
        }

def is_outdoor_friendly(weather):
    # Outdoor-friendly if condition is Clear, Sunny or Partly Cloudy and temp below 35°C
    return weather["condition"] in ["Clear", "Sunny", "Partly Cloudy"] and weather["temp"] < 35
def get_weather_mood_quote(condition):
    condition = condition.lower()
    if "rain" in condition:
        return "☔  Perfect day for a hot snack and chai indoors!"
    elif "clear" in condition or "sunny" in condition:
        return "☀️  Great day to soak up the sun with street food!"
    elif "cloud" in condition:
        return "🌥️  Slightly cloudy – nice for a relaxed foodie walk!"
    elif "snow" in condition:
        return "❄️  Cozy up with something warm and comforting!"
    else:
        return "🌡️  Weather’s mixed – a foodie adventure awaits!"