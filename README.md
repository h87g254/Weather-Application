# Weather Project

This is a Django-based web application that fetches and displays weather information for a given city using the OpenWeatherMap API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Docker Setup](#docker-setup)
- [Running the Project](#running-the-project)
- [Testing](#testing)

## Introduction

The Weather Project is a web application built with Django that allows users to get current weather information for any city. It uses the OpenWeatherMap API to fetch weather data and displays it in a user-friendly interface.

## Features

- Fetches current weather data for any city.
- Displays temperature, humidity, wind speed, and weather conditions.
- Responsive design for mobile and desktop views.
- Docker support for easy deployment.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/h87g254/Weather-Application.git
    cd weather_project
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv weather_venv
    weather_venv\Scripts\activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Set up the environment variables as described in the [Environment Variables](#environment-variables) section.
2. Run the Django development server:
    ```sh
    python manage.py runserver
    ```
3. Open your web browser and navigate to `http://127.0.0.1:8000`.


## Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:

API_KEY=<your_openweathermap_api_key>


## Docker Setup

1. Build the Docker image:
    ```sh
    docker-compose build
    ```

2. Run the Docker container:
    ```sh
    docker-compose up
    ```

3. Open your web browser and navigate to `http://127.0.0.1:8000`.

## Running the Project

1. Apply migrations:
    ```sh
    python manage.py migrate
    ```

2. Run the development server:
    ```sh
    python manage.py runserver
    ```

3. Open your web browser and navigate to `http://127.0.0.1:8000`.

## Testing

To run tests, use the following command:
```sh
python manage.py test

