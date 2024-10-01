import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather(city="cairo"):
    print("\n*** Get Current weahter conditions ***\n")

    # city = input("\nPlease enter a city name:\n")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    # print(request_url)
    
    weather_data = requests.get(request_url).json()
    
    # pprint(weather_data)
    
    # print(f"\nCurrent weather for {weather_data['name']}")
    # print(f"\nTemp for {weather_data['main']['temp']}")
    # print(f"\nFeels like {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description'].upper()}")
    
    return weather_data


if __name__ == "__main__":
    print("/n*** Get the Current Weather condition ***\n")
    
    city = input("\nPlease enter a city name: ")
    if not city.strip():
        city = "alex"
    weather_data = get_current_weather(city)

    pprint(weather_data)