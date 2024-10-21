namespace Weather_Application_Csharp.Models
{
    public class WeatherResponse
    {
        public string Description { get; set; }
        public string City { get; set; }
        public double Temperature { get; set; }
        public int Humidity { get; set; }
        public double WindSpeed { get; set; }
        public string Icon { get; set; }
    }
}