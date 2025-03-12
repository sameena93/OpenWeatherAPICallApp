import requests
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime, timedelta, timezone

API_key = os.getenv("WHEATHER_API_KEY")


# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# call api with requests

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

    response = requests.get(url)
    if response.status_code ==200:
        
        

        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like_kelvin = data['main']['feels_like']  # Feels like is usually in Kelvin
        
        # Convert `feels_like` from Kelvin to Fahrenheit and Celsius
        feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
        temp_celsius = kelvin_to_celsius(temp)
        humidity = data['main']['humidity']
        visibility = data.get('visibility', 'N/A')
        name = data['name']
        country = data['sys']['country']
        timezone_offset = data['timezone']
        sunrise= datetime.fromtimestamp(data['sys']['sunrise'] + timezone_offset, tz=timezone.utc).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']+ timezone_offset, tz=timezone.utc).strftime('%H:%M:%S')

        print(
            f"\n Weather in {name}, {country}:\n"
            f"🌤️\t Weather    : {weather.capitalize()}\n"
            f"🌡️\t Temperature: {round(temp_celsius)}°F \n"
            f"🌡️\t Feels like : {round(feels_like_celsius)}°C \n" 
            f"💧\t Humidity   : {humidity}%\n"
            f"👁️\t Visibility : {visibility} meters\n"
            f"🌅\t Sunrise    : {sunrise} (Local Time)\n"
            f"🌇\t Sunset     : {sunset} (Local Time)\n"
        )
    else:
        print("Error: City not found or API limit reached.")

def main():
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        
        if city.lower() == "exit":
            print("Exiting the program.")
            break
        
        get_weather(city)


if __name__ == "__main__":
    main()

    
# python get_wheather.py
