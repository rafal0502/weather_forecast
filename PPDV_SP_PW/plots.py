from datetime import datetime, timedelta
from typing import List

from model.City import City


def customize(axis, **kwargs):
    axis.clear()
    axis.set_title(kwargs['title'])
    axis.tick_params(labelsize=6)
    axis.set_ylabel(kwargs['y_label'])
    return axis


def plot_temperature(axis, forecast_data):
    temperature = [forecast.temp for forecast in forecast_data]
    x = [data.datetime_txt[11:16] for data in forecast_data]
    axis = customize(axis, title="Temperature", y_label="°C")
    axis.plot(x, temperature, '.-', color="red")


def plot_pressure(axis, forecast_data):
    pressure = [forecast.grnd_level for forecast in forecast_data]
    x = [data.datetime_txt[11:16] for data in forecast_data]
    axis = customize(axis, title="Pressure", y_label="hPa")
    axis.set_ylim([min(pressure), max(pressure) + 1])
    axis.plot(x, pressure, '.-', color="yellow")
    d = [min(pressure)] * len(pressure)
    axis.fill_between(x, pressure, where=pressure >= d, interpolate=True, color="yellow")


def plot_humidity(axis, forecast_data):
    humidity = [forecast.humidity for forecast in forecast_data]
    x = [data.datetime_txt[11:16] for data in forecast_data]
    axis = customize(axis, title="Humidity", y_label="%")
    axis.set_ylim([min(humidity) - 10, 100])
    axis.plot(x, humidity, '.-')
    d = [min(humidity)] * len(humidity)
    axis.fill_between(x, humidity, where=humidity >= d, interpolate=True)


def plot_cloud(axis, forecast_data):
    cloud = [forecast.cloud_percentage for forecast in forecast_data]
    x = [data.datetime_txt[11:16] for data in forecast_data]
    axis = customize(axis, title="Clouds", y_label="%")
    axis.plot(x, cloud, '.-', color="gray")
    axis.set_ylim([0, 100])
    d = [0] * len(cloud)
    axis.fill_between(x, cloud, where=cloud >= d, interpolate=True, color="gray")


def plot_rain(axis, forecast_data):
    rain = [forecast.rain_in_last_3_hours for forecast in forecast_data]
    x = [data.datetime_txt[11:16] for data in forecast_data]
    axis = customize(axis, title="Rain", y_label="mm")
    axis.bar(x, rain, width=1)


def plot2D(self):
    cities: List[City] = self.adapter.get_basic_forecast_data()
    city_id = [city.city_id for city in cities if city.name == self.city_combo_box.currentText()][0]
    date = self.date_combo_box.currentText()
    begin = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    city = [x for x in cities if x.city_id == city_id][0]
    forecast_data = city.forecast.get_forecast(begin - timedelta(hours=3),
                                               begin + timedelta(days=1))

    self.lat_lon_label.setText(f"{city.name}: latitude {city.latitude:4.4f}, longitude {city.longitude:4.4f}.")
    self.title_label.setText("WEATHER DETAILS")
    self.temperature_label.setText(f"Temperature: {forecast_data[0].temp:5.2f}°C,"
                                   f" max: {forecast_data[0].temp_max:5.2f}°C,"
                                   f" min: {forecast_data[0].temp_min:5.2f}°C.")
    self.pressure_label.setText(f"Pressure: {forecast_data[0].grnd_level:5.2f} hPa,"
                                f" {forecast_data[0].sea_level:5.2f}hPa.")
    self.precipitation_label.setText(f"In next 3 hours: rain - {forecast_data[1].rain_in_last_3_hours:5.2f} mm,"
                                     f" snow - {forecast_data[1].snow_in_last_3_hours:5.2f} mm.")

    # create an axis
    temperature_axis = self.figure.add_subplot(911)
    pressure_axis = self.figure.add_subplot(913)
    humidity_axis = self.figure.add_subplot(915)
    cloud_axis = self.figure.add_subplot(917)
    rain_axis = self.figure.add_subplot(919)

    plot_temperature(temperature_axis, forecast_data)
    plot_pressure(pressure_axis, forecast_data)
    plot_humidity(humidity_axis, forecast_data)
    plot_cloud(cloud_axis, forecast_data)
    plot_rain(rain_axis, forecast_data)

    # refresh canvas
    self.canvas.draw()
