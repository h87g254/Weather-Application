# Weather Application

This is a simple ASP.NET Core web application that fetches and displays weather information for a specified city using the OpenWeatherMap API.

## Features

- Fetches weather data including temperature, humidity, wind speed, and weather description.
- Displays weather information in a clean and modern UI.
- Uses Razor Pages and ASP.NET Core for the backend.
- Configurable via `appsettings.json`.

## Prerequisites

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
- [Visual Studio 2022](https://visualstudio.microsoft.com/vs/)
- [OpenWeatherMap API Key](https://openweathermap.org/api)

## Getting Started

### Clone the Repository

```sh
git clone https://github.com/yourusername/Weather-Application.git
cd Weather-Application
```

### Configuration 

1. Add your OpenWeatherMap API Key

- Make file named `appsettings.json`

- In it add this 

```json
{
  "OpenWeatherMap": {
    "ApiKey": "YOUR_API_KEY"
  },
  "Logging": {
    "Level": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
    }
  },
  "AllowedHosts": "*"
}
```

2. Optional: Configure Development Settings

-Open `Weather Application Csharp/appsettings.Development.json` for development-specific settings.

### Build and Run

1. Open the Solution in Visual Studio:

- Open `Weather Application Csharp.sln` in Visual Studio 2022.

2. Set the Startup Project:

- In the Solution Explorer, right-click on `Weather Application Csharp` and select `Set as Startup Project`.

3. Run the Application:

- Click the green play button or press `F5` to build and run the application.
- The application should open in your default web browser at `https://localhost:7040` or `http://localhost:5220`.

### Using the Application

1. Enter a City:

- On the home page, enter the name of a city in the input field and click "Get Weather".

2. View Weather Information:

- The application will fetch and display the weather information for the specified city, including temperature, humidity, wind speed, and weather description.

### Summary

- **Project Overview**: Describes the project and its features.
- **Prerequisites**: Lists the required tools and API key.
- **Getting Started**: Provides steps to clone, configure, build, and run the project.
