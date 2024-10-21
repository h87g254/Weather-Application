using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;
using Weather_Application_Csharp.Models;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;

namespace Weather_Application_Csharp.Services
{
    public class WeatherService
    {
        private readonly HttpClient _httpClient;
        private readonly string _apiKey;
        private readonly ILogger<WeatherService> _logger;

        public WeatherService(HttpClient httpClient, IConfiguration configuration, ILogger<WeatherService> logger)
        {
            _httpClient = httpClient;
            _apiKey = configuration["OpenWeatherMap:ApiKey"];
            _logger = logger;
        }

        public async Task<WeatherResponse> GetWeatherAsync(string city)
        {
            try
            {
                var response = await _httpClient.GetStringAsync($"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={_apiKey}&units=metric");
                var data = JObject.Parse(response);

                return new WeatherResponse
                {
                    City = data["name"].ToString(),
                    Description = data["weather"][0]["description"].ToString(),
                    Temperature = double.Parse(data["main"]["temp"].ToString()),
                    Humidity = int.Parse(data["main"]["humidity"].ToString()),
                    WindSpeed = double.Parse(data["wind"]["speed"].ToString()),
                    Icon = data["weather"][0]["icon"].ToString()
                };
            }
            catch (HttpRequestException e)
            {
                _logger.LogError($"Request error: {e.Message}");
                return null;
            }
            catch (JsonException e)
            {
                _logger.LogError($"JSON parsing error: {e.Message}");
                return null;
            }
            catch (Exception e)
            {
                _logger.LogError($"Unexpected error: {e.Message}");
                return null;
            }
        }
    }
}