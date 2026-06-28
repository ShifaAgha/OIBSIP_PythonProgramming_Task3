# Weather App — OIBSIP Python Programming, Task 3

A command-line weather app in Python that fetches and displays real-time
weather data for any city or US ZIP code using the OpenWeatherMap API.

## Features

- Search by city name (e.g. `London`, `Karachi`, `New York`) or US ZIP code
- Displays current weather conditions, temperature (°C and °F), feels-like,
  min/max temp, humidity, wind speed, and visibility
- Handles invalid city names, bad API keys, and no-internet errors gracefully
- Allows multiple searches in one session

## Setup

### 1. Get a Free API Key
- Go to https://openweathermap.org/api and sign up (free)
- After signing in, go to **API Keys** tab and copy your key
- Note: new keys can take up to 10 minutes to activate

### 2. Add Your API Key
Open `weather_app.py` and replace `YOUR_API_KEY_HERE` with your actual key:
```python
API_KEY = "your_actual_key_here"
```

### 3. Install Dependency
```bash
pip install requests
```

### 4. Run
```bash
python weather_app.py
```

## Example Output

```
==================================================
   Weather App - OIBSIP Python Task 3
==================================================
Enter a city name (e.g. London)
or a US ZIP code  (e.g. 10001)
Type 'exit' to quit.
==================================================

Enter city or ZIP code: Karachi

==================================================
   Weather in Karachi, PK
==================================================
  Condition     : Clear Sky
  Temperature   : 33.2°C  /  91.8°F
  Feels Like    : 35.1°C  /  95.2°F
  Min / Max     : 32.0°C  /  34.5°C
  Humidity      : 60%
  Wind Speed    : 4.1 m/s
  Visibility    : 6 km
==================================================
```

## Key Concepts Used

- **API Integration** — connects to OpenWeatherMap REST API using `requests`
- **JSON Parsing** — extracts and formats data from the API response
- **Input Validation** — auto-detects ZIP codes vs city names, handles empty input
- **Error Handling** — covers 401 (bad key), 404 (city not found), timeouts, no internet
- **Unit Conversion** — converts Celsius to Fahrenheit automatically

## Project Structure

```
ShifaAgha_Task3/
├── weather_app.py   # main program
└── README.md        # this file
```

## Author

Shifa Agha — OIBSIP Python Programming Internship
GitHub: https://github.com/ShifaAgha/OIBSIP
