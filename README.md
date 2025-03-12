# Weather Information App (API)

A simple weather information app that fetches real-time weather details from the OpenWeather API based on the city name entered by the user. The application provides information such as weather description, temperature in Celsius , humidity, visibility, sunrise, and sunset times.

---

## Skills
This project demonstrates the following skills:

### Programming Languages:
* ***Python:*** The primary language used for this project.
Libraries Used:
* ***Requests:*** Used to make HTTP requests to the OpenWeather API and retrieve weather data.
* ***os:*** Used for environment variable management, loading the API key securely.
* ***datetime:*** Used to handle and format date/time information, specifically to convert Unix timestamps to readable times for sunrise and sunset.
  

![file](https://github.com/sameena93/OpenWeatherAPICallApp/blob/main/statics/Demo.jpg)

---

## Features
* Fetches current weather details for any city entered by the user.
* Displays
    1. Weather description (e.g., clear sky, broken clouds, etc.)
    2. Temperature in Celsius and Fahrenheit
    3. Feels like temperature in Celsius and Fahrenheit
    4. Humidity percentage
    5. Visibility distance in meters
    6. Sunrise and sunset times in the local timezone
* Interactive command-line interface where users can input the city name to get weather details.

---

## Prerequisites
Before running the project, make sure you have the following installed:
* Python 3.12
* pip (Python package manager)

---

## Dependencies
You will need to install the following Python packages:

* requests: Used to make HTTP requests to the OpenWeather API.
* python-dotenv: Loads environment variables from a .env file (for storing API keys).

---

### API Usage
OpenWeather API
This project uses the !(OpenWeather API)[https://dashboard.openweather.co.uk/] to fetch real-time weather data.

