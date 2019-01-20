from GetForecast import *



g = GetForecast()

weatherWarsaw= g.get_forecast_for_city("Warszawa")
print(weatherWarsaw)


weather = g.get_basic_forecast_data()
print(weather)