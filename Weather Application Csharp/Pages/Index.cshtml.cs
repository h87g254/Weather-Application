using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Weather_Application_Csharp.Models;
using Weather_Application_Csharp.Services;

namespace Weather_Application_Csharp.Pages
{
    public class IndexModel : PageModel
    {
        private readonly WeatherService _weatherService;

        public IndexModel(WeatherService weatherService)
        {
            _weatherService = weatherService;
        }

        [BindProperty]
        public string City { get; set; }

        public WeatherResponse Weather { get; set; }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!string.IsNullOrEmpty(City))
            {
                Weather = await _weatherService.GetWeatherAsync(City);
            }
            return Page();
        }
    }
}