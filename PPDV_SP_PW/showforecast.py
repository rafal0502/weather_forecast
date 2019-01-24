import json
from datetime import datetime, timedelta
from typing import List

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from ResponseAdapter import ResponseAdapter
from forecast_3d.map_qwidget import MapWidget
from input_file_api import InputOperations
from mainwindow import Ui_MainWindow
from model.City import City
from plots import plot2D


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)
        input_operations = InputOperations(kwargs["adapter"])
        self.city_combo_box.addItems(input_operations.cities_names)
        self.date_combo_box.addItems(input_operations.possible_dates)
        self.adapter: ResponseAdapter = kwargs["adapter"]
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.start_button.clicked.connect(self.plot)
        self.plots_layout.addWidget(self.canvas)
        self.cities = kwargs["cities"]

        self.map_widget = MapWidget(
            parent=self.widget3d,
            geographical_boundaries=kwargs["boundaries"],
            adapter=self.adapter,
            cities=kwargs["cities"]
        )

        self.threadpool = QThreadPool()
        self.plot()
        self.show()

    def plot(self):
        plot2D(self)

        date = self.date_combo_box.currentText()
        begin = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        city_by_hour_prediction = [(city.city_id, city.forecast.get_forecast(begin-timedelta(minutes=1), begin+timedelta(minutes=1))) for city in self.cities]
        self.map_widget.render_3d_map(city_by_hour_prediction, {
            'temp': self.temperature_check_box.isChecked(),
            'pres': self.pressure_check_box.isChecked(),
            'clouds': self.clouds_check_box.isChecked(),
            'pre': self.precipitation_check_box.isChecked(),
            'wind': self.wind_check_box.isChecked()
        })

    def resizeEvent(self, event):
        self.map_widget.update_size()


def main():
    app = QApplication([])
    with open('input_data_config.json') as f:
        data = json.load(f)
    adapter = ResponseAdapter()
    cities: List[City] = adapter.get_forecast_data(data["cities"])
    print(cities[0].forecast.get_forecast(datetime.now(), datetime.now() + timedelta(days=1)))
    window = MainWindow(adapter=adapter, boundaries=data["bounds"], cities=cities)
    app.exec_()


if __name__ == '__main__':
    main()
