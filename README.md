# Weather App

This is a simple Django-based web application that fetches and displays weather information for a specified city using the OpenWeatherMap API.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Key](#api-key)
- [Running the Application](#running-the-application)
- [Screenshots](#screenshots)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/weather_app.git
    cd weather_app
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv weather_venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
        ```sh
        weather_venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source weather_venv/bin/activate
        ```

4. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. **API Key:**
    - Obtain an API key from /api[OpenWeatherMap](https://openweathermap.org).
    - Replace `'YOUR_API_KEY'` in [views.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cdanie%5C%5CDesktop%5C%5CWeather%20App%5C%5Cweather_project%5C%5Cweather_app%5C%5Cviews.py%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fdanie%2FDesktop%2FWeather%20App%2Fweather_project%2Fweather_app%2Fviews.py%22%2C%22scheme%22%3A%22file%22%7D%7D) with your actual API key.

2. **Database:**
    - The project uses SQLite by default. The database file is located at [db.sqlite3](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cdanie%5C%5CDesktop%5C%5CWeather%20App%5C%5Cweather_project%5C%5Cdb.sqlite3%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fdanie%2FDesktop%2FWeather%20App%2Fweather_project%2Fdb.sqlite3%22%2C%22scheme%22%3A%22file%22%7D%7D).

## Usage

1. **Run the Django development server:**

    ```sh
    python weather_project/manage.py runserver
    ```

2. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

3. **Enter a city name in the input field and submit to get the weather information.**

## Project Structure

weather_app/ ├── .gitignore ├── requirements.txt ├── weather_project/ │ ├── db.sqlite3 │ ├── manage.py │ ├── weather_app/ │ │ ├── init.py │ │ ├── pycache/ │ │ ├── admin.py │ │ ├── apps.py │ │ ├── migrations/ │ │ ├── models.py │ │ ├── templates/ │ │ │ └── weather_app/ │ │ │ └── index.html │ │ ├── tests.py │ │ ├── urls.py │ │ ├── views.py │ ├── weather_project/ │ │ ├── init.py │ │ ├── pycache/ │ │ ├── asgi.py │ │ ├── settings.py │ │ ├── urls.py │ │ ├── wsgi.py ├── weather_venv/ │ ├── Include/ │ ├── Lib/ │ │ └── site-packages/ │ ├── pyvenv.cfg │ ├── Scripts/ │ │ ├── activate │ │ ├── activate.bat │ │ ├── Activate.ps1 │ │ ├── deactivate.bat │ │ ├── django-admin.exe │ │ ├── normalizer.exe │ │ ├── pip.exe │ │ ├── pip3.12.exe │ │ ├── pip3.exe


## API Key

To use the OpenWeatherMap API, you need an API key. Follow these steps to get one:

1. Go to [OpenWeatherMap](https://openweathermap.org/api) and sign up for an account.
2. Navigate to the API keys section in your account.
3. Generate a new API key.
4. Replace `'YOUR_API_KEY'` in [`weather_project/weather_app/views.py`](weather_project/weather_app/views.py) with your actual API key.

## Running the Application

1. **Start the Django development server:**

    ```sh
    python weather_project/manage.py runserver
    ```

2. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

3. **Enter a city name in the input field and submit to get the weather information.**

## Screenshots

![Weather App Screenshot](path/to/screenshot.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
