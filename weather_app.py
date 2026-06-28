"""
Weather App (Beginner Level) - OIBSIP Python Programming Task 3
---------------------------------------------------------------
Features:
    1. Prompts user for a city name or ZIP code.
    2. Fetches current weather data from OpenWeatherMap API.
    3. Displays temperature, humidity, and weather conditions.
    4. Handles invalid city names, network errors, and bad API keys.
    5. Allows multiple searches without restarting.

Setup:
    1. Get a FREE API key from https://openweathermap.org/api
    2. Replace YOUR_API_KEY_HERE below with your actual key.
    3. pip install requests
    4. python weather_app.py
"""

import requests

# ---------------------------------------------------------------
# PASTE YOUR OPENWEATHERMAP API KEY HERE
# ---------------------------------------------------------------
API_KEY = "2c995bb3bc763edc1f5cc7923909f166"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(location):
    """
    Fetch weather data for a city name or ZIP code.
    Returns a dict on success, None on failure.
    """
    # Determine if input looks like a US ZIP code (5 digits)
    if location.strip().isdigit() and len(location.strip()) == 5:
        params = {
            "zip": f"{location.strip()},us",
            "appid": API_KEY,
            "units": "metric",
        }
    else:
        params = {
            "q": location.strip(),
            "appid": API_KEY,
            "units": "metric",
        }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print("\n  ERROR: Invalid API key.")
            print("  Please check your API key at https://openweathermap.org/api\n")
        elif response.status_code == 404:
            print(f"\n  ERROR: Location '{location}' not found.")
            print("  Try a different city name or check the spelling.\n")
        else:
            print(f"\n  ERROR: Unexpected response (status {response.status_code}).\n")

    except requests.exceptions.ConnectionError:
        print("\n  ERROR: No internet connection. Please check your network.\n")
    except requests.exceptions.Timeout:
        print("\n  ERROR: Request timed out. Please try again.\n")
    except requests.exceptions.RequestException as e:
        print(f"\n  ERROR: {e}\n")

    return None


def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 1)


def display_weather(data):
    """Print weather data in a clean, readable format."""
    city        = data["name"]
    country     = data["sys"]["country"]
    condition   = data["weather"][0]["description"].title()
    temp_c      = data["main"]["temp"]
    feels_c     = data["main"]["feels_like"]
    temp_min_c  = data["main"]["temp_min"]
    temp_max_c  = data["main"]["temp_max"]
    humidity    = data["main"]["humidity"]
    wind_speed  = data["wind"]["speed"]
    visibility  = data.get("visibility", "N/A")

    temp_f      = celsius_to_fahrenheit(temp_c)
    feels_f     = celsius_to_fahrenheit(feels_c)

    print("\n" + "=" * 50)
    print(f"   Weather in {city}, {country}")
    print("=" * 50)
    print(f"  Condition     : {condition}")
    print(f"  Temperature   : {temp_c}°C  /  {temp_f}°F")
    print(f"  Feels Like    : {feels_c}°C  /  {feels_f}°F")
    print(f"  Min / Max     : {temp_min_c}°C  /  {temp_max_c}°C")
    print(f"  Humidity      : {humidity}%")
    print(f"  Wind Speed    : {wind_speed} m/s")
    if visibility != "N/A":
        print(f"  Visibility    : {visibility // 1000} km")
    print("=" * 50 + "\n")


def main():
    print("=" * 50)
    print("   Weather App - OIBSIP Python Task 3")
    print("=" * 50)
    print("  Enter a city name (e.g. London)")
    print("  or a US ZIP code  (e.g. 10001)")
    print("  Type 'exit' to quit.")
    print("=" * 50 + "\n")

    if API_KEY == "YOUR_API_KEY_HERE":
        print("  WARNING: You have not set your API key yet!")
        print("  Get a free key at https://openweathermap.org/api")
        print("  Then replace YOUR_API_KEY_HERE in weather_app.py\n")

    while True:
        location = input("Enter city or ZIP code: ").strip()

        if not location:
            print("  Please enter a location.\n")
            continue

        if location.lower() in ("exit", "quit", "bye"):
            print("\nGoodbye! Stay weather-aware!")
            break

        data = get_weather(location)
        if data:
            display_weather(data)

        again = input("Search another location? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nGoodbye! Stay weather-aware!")
            break
        print()


if __name__ == "__main__":
    main()
