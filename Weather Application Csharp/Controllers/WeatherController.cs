using Microsoft.AspNetCore.Mvc;
using Weather_Application_Csharp.Services;

namespace Weather_Application_Csharp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class WeatherController : ControllerBase
    {
        private readonly WeatherService _weatherService;

        public WeatherController(WeatherService weatherService)
        {
            _weatherService = weatherService;
        }

        [HttpGet("{city}")]
        public async Task<IActionResult> GetWeather(string city)
        {
            var weather = await _weatherService.GetWeatherAsync(city);
            if (weather == null)
            {
                return NotFound();
            }
            return Ok(weather);
        }
    }
}