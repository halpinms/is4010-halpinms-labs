import requests
from typing import Optional, Dict, Any
import config

class WeatherAPI:
    """
    Client for fetching weather data from WeatherAPI.com.

    Parameters
    ----------
    api_key : str
        The API key for WeatherAPI.com.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = config.WEATHER_API_BASE_URL

    def get_current_weather(self, location: str) -> Optional[Dict[str, Any]]:
        """
        Fetch current weather for a given location.

        Parameters
        ----------
        location : str
            City name or favorite name.

        Returns
        -------
        Optional[Dict[str, Any]]
            Weather data dictionary or None if error.
        """
        try:
            url = f"{self.base_url}/current.json"
            params = {
                "key": self.api_key,
                "q": location,
                "aqi": "no"
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

    def get_forecast(self, location: str, days: int = 3) -> Optional[Dict[str, Any]]:
        """
        Fetch weather forecast for a given location.

        Parameters
        ----------
        location : str
            City name or favorite name.
        days : int, optional
            Number of days (1-3). Defaults to 3.

        Returns
        -------
        Optional[Dict[str, Any]]
            Forecast data dictionary or None if error.
        """
        try:
            url = f"{self.base_url}/forecast.json"
            params = {
                "key": self.api_key,
                "q": location,
                "days": days,
                "aqi": "no",
                "alerts": "no"
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

def format_current_weather(data: Dict[str, Any]) -> str:
    """
    Format current weather data for display.

    Parameters
    ----------
    data : Dict[str, Any]
        API response data.

    Returns
    -------
    str
        Formatted weather string.
    """
    location = data.get("location", {})
    current = data.get("current", {})
    
    name = location.get("name")
    country = location.get("country")
    condition = current.get("condition", {}).get("text")
    temp_f = current.get("temp_f")
    temp_c = current.get("temp_c")
    feelslike_f = current.get("feelslike_f")
    feelslike_c = current.get("feelslike_c")
    humidity = current.get("humidity")
    wind_mph = current.get("wind_mph")
    wind_dir = current.get("wind_dir")
    last_updated = current.get("last_updated")

    output = []
    output.append("=" * 50)
    output.append(f"Current Weather for {name}, {country}")
    output.append("=" * 50)
    output.append(f"Condition: {condition}")
    output.append(f"Temperature: {temp_f}°F ({temp_c}°C)")
    output.append(f"Feels Like: {feelslike_f}°F ({feelslike_c}°C)")
    output.append(f"Humidity: {humidity}%")
    output.append(f"Wind: {wind_mph} mph {wind_dir}")
    output.append(f"Last Updated: {last_updated}")
    output.append("=" * 50)
    
    return "\n".join(output)

def format_forecast(data: Dict[str, Any]) -> str:
    """
    Format forecast weather data for display.

    Parameters
    ----------
    data : Dict[str, Any]
        API response data.

    Returns
    -------
    str
        Formatted forecast string.
    """
    location = data.get("location", {})
    name = location.get("name")
    country = location.get("country")
    forecast_days = data.get("forecast", {}).get("forecastday", [])

    output = []
    output.append("=" * 50)
    output.append(f"Forecast for {name}, {country}")
    output.append("=" * 50)

    for day_data in forecast_days:
        date = day_data.get("date")
        day = day_data.get("day", {})
        condition = day.get("condition", {}).get("text")
        max_temp_f = day.get("maxtemp_f")
        min_temp_f = day.get("mintemp_f")
        
        output.append(f"Date: {date}")
        output.append(f"Condition: {condition}")
        output.append(f"High: {max_temp_f}°F, Low: {min_temp_f}°F")
        output.append("-" * 20)

    output.append("=" * 50)
    
    return "\n".join(output)
