# Django Weather App

A simple Django application that fetches and displays weather information based on user input. This app uses the WeatherAPI to retrieve current weather data for a specified city.

## Test the App Here
https://weatherapp-production-8302.up.railway.app/
(Demo Server is slower than the Actual App)

## Features

- Users can enter the name of a city to get the current weather information.
- Displays city name, region, country, last updated time, temperature in Celsius and Fahrenheit, feels-like temperature, weather description, and an icon representing the current weather condition.
- Light mode and dark mode support based on whether it is day or night in the specified city.

## Installation

1. **Clone the repository, create a virtual environment, and install dependencies**:
   ```bash
   git clone https://github.com/yourusername/django-weather-app.git
   cd django-weather-app
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

## Set up your API key:

1. **Sign up at [WeatherAPI](https://www.weatherapi.com/) to get your API key.**

2. **Replace the placeholder `api` value in `views.py` with your actual API key**:
   ```python
   api = "your_api_key_here"
   ```

## Run the Django development server:

1. **Start the server**:
   ```bash
   python manage.py runserver
   ```

## Access the Application:

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Usage

### Home Page

- The home page contains a simple form where you can enter the name of a city.

### Weather Report

- Upon submission, the app will display the current weather data for the specified city.
- If the city name is invalid or not found, an error message will be displayed.


### Screenshots
![Screenshot_26-8-2024_13270_127 0 0 1](https://github.com/user-attachments/assets/cbcb1d8c-4d61-431b-ad5b-f945e2298974)
![Screenshot_26-8-2024_132732_127 0 0 1](https://github.com/user-attachments/assets/0c244d49-a537-4aea-b96c-65297c5cac74)
![Screenshot_26-8-2024_13280_127 0 0 1](https://github.com/user-attachments/assets/320018ac-f024-4ed9-8a11-aed5cedb629b)
