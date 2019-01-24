from typing import List

import vtk
from PyQt5.QtWidgets import *

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

import ResponseAdapter
from forecast_3d.cloud_actors import cloud_actor
from forecast_3d.legend import legend_actor, tem_col, p_col
from forecast_3d.prec_actors import prec_actor
from forecast_3d.pressure_actors import pressure_actor
from forecast_3d.temperature_actors import temperature_actor
from forecast_3d.wind_actors import wind_actor
from model.City import City


class MapWidget:
    def __init__(self, parent: QWidget, geographical_boundaries: dict, adapter: ResponseAdapter, cities: List[City]):
        self.parent = parent
        self.boundaries = geographical_boundaries
        self.adapter: ResponseAdapter = adapter
        self.cities: List[City] = cities
        self.vtk_widget = QVTKRenderWindowInteractor(parent)
        self.renderer = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)
        self.interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        self.normalized_cities: List[dict] = []
        self.actors = {'precipitation': [], 'clouds': [], 'wind': [], 'temperature': [], 'pressure': []}

        self.map3d_actor = None

        self.legend_actors = []

        self.initialize_map()
        self.update_size()
        self.interactor.Initialize()
        self.renderer.GetActiveCamera().Elevation(-15)
        self.renderer.ResetCamera()

    def update_size(self):
        self.vtk_widget.resize(self.parent.size())
        for city in self.cities:
            (vtk_x, vtk_y) = self.transform_coordinates(city)
            self.normalized_cities.append({
                "city_id": city.city_id,
                "x": vtk_x,
                "y": vtk_y
            })
        self.legend_init()

    def initialize_map(self):
        reader = vtk.vtkPNGReader()
        reader.SetFileName("images/pl_map.png")
        reader.Update()

        filter = vtk.vtkImageDataGeometryFilter()
        filter.SetInputConnection(reader.GetOutputPort())
        filter.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(filter.GetOutputPort())

        self.map3d_actor = vtk.vtkActor()
        self.map3d_actor.SetMapper(mapper)
        self.renderer.AddActor(self.map3d_actor)

    def render_3d_map(self, data: List, checks: dict):
        self.renderer.RemoveAllViewProps()
        self.initialize_map()
        for city in data:
            ct = next(item for item in self.normalized_cities if item["city_id"] == city[0])
            if len(city[1]) > 0:
                if checks['clouds']:
                    self.renderer.AddActor(cloud_actor(ct["x"], ct["y"], city[1][0].cloud_percentage))

                if checks['pres']:
                    pres_col = None
                    for i in range(950, 1055, 10):
                        if city[1][0].pressure < i:
                            pres_col = p_col.GetColor3d('<' + str(i))
                            break
                    if pres_col is None:
                        pres_col = p_col.GetColor3d('>=1050')
                    p_actor, text_p_actor = pressure_actor(ct["x"], ct["y"], city[1][0].pressure, pres_col)
                    self.renderer.AddActor(p_actor)
                    self.renderer.AddActor(text_p_actor)

                if checks['temp']:
                    temp_col = None
                    for i in range(-20, 35, 5):
                        if city[1][0].temp < i:
                            temp_col = tem_col.GetColor3d('<' + str(i))
                            break
                    if temp_col is None:
                        temp_col = tem_col.GetColor3d('>=30')
                    t_actor, text_t_actor = temperature_actor(ct["x"], ct["y"], city[1][0].temp, temp_col)
                    self.renderer.AddActor(t_actor)
                    self.renderer.AddActor(text_t_actor)

                if checks['pre']:
                    self.renderer.AddActor(prec_actor(ct["x"], ct["y"], city[1][0].rain_in_last_3_hours + city[1][0].snow_in_last_3_hours))

                if checks['wind']:
                    self.renderer.AddActor(wind_actor(ct["x"], ct["y"], city[1][0].wind_speed, city[1][0].wind_direction))

        self.legend_init()
        self.vtk_widget.update()

    @staticmethod
    def normalize_coordinates(val, min, max):
        return (val - min) / (max - min)

    def transform_coordinates(self, city_coordinates: City):
        vtk_width = self.map3d_actor.GetBounds()[1]
        vtk_height = self.map3d_actor.GetBounds()[3]

        vtk_x = MapWidget.normalize_coordinates(
            city_coordinates.longitude,
            self.boundaries['left'],
            self.boundaries['right']
        ) * vtk_width

        vtk_y = MapWidget.normalize_coordinates(
            city_coordinates.latitude,
            self.boundaries['lower'],
            self.boundaries['upper']
        ) * vtk_height

        return vtk_x, vtk_y

    def legend_init(self):
        if len(self.legend_actors) > 0:
            for actor in self.legend_actors:
                self.renderer.RemoveActor(actor)

        self.legend_actors = legend_actor(self.vtk_widget.size().width(), self.vtk_widget.size().height())
        for actor in self.legend_actors:
            self.renderer.AddActor(actor)
