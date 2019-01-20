from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk

from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app: QApplication, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.app: QApplication = app
        self.setupUi(self)

        self.chooseFileBtt.pressed.connect(self.choose_file)
        self.quitBtt.pressed.connect(self.close_app)
        self.loadBtt.pressed.connect(self.load_btt)
        self.deleteBtt.pressed.connect(self.del_btt)

        self.vtk_widget = QVTKRenderWindowInteractor(self.widget)
        self.vtk_widget.resize(self.widget.size())
        self.renderer = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)
        self.interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

        self.interactor.Initialize()
        self.renderer.GetActiveCamera().Elevation(-15)
        self.renderer.ResetCamera()

        self.model = QStandardItemModel()
        self.model.itemChanged.connect(self.render_view)
        self.listView.setModel(self.model)
        self.listView.show()

        self.threadpool = QThreadPool()

        self.show()

    def choose_file(self):
        self.filePath_edit.setText(QFileDialog.getOpenFileName(self, 'Open file', '', 'STL file (*.stl)')[0])

    def close_app(self):
        self.app.quit()

    def load_btt(self):
        path = self.filePath_edit.text()
        if (path != ""):
            is_on_list = False
            i = 0
            while self.model.item(i):
                if self.model.item(i).text() == path:
                    is_on_list = True
                i += 1
            if not is_on_list:
                item = QStandardItem(path)
                item.setCheckState(Qt.Unchecked)
                item.setCheckable(True)
                self.model.appendRow(item)

    def del_btt(self):
        i = 0
        while self.model.item(i):
            if self.model.item(i).checkState():
                self.model.removeRow(i)
            i += 1

        self.render_view()

    def render_view(self):
        self.renderer.RemoveAllViewProps()
        i = 0
        while self.model.item(i):
            if self.model.item(i).checkState():
                cloud_source = vtk.vtkSTLReader()
                cloud_source.SetFileName(self.model.item(i).text())

                translation = vtk.vtkTransform()
                translation.Scale(1, 1, 1)
                transform_filter = vtk.vtkTransformPolyDataFilter()
                transform_filter.SetTransform(translation)
                transform_filter.SetInputConnection(cloud_source.GetOutputPort())

                mapper = vtk.vtkPolyDataMapper()
                mapper.SetInputConnection(transform_filter.GetOutputPort())

                actor = vtk.vtkActor()
                actor.SetMapper(mapper)
                actor.SetVisibility(True)

                self.renderer.AddActor(actor)

                print(self.model.item(i).text())
            i += 1
        self.vtk_widget.update()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow(app)
    app.exec_()
