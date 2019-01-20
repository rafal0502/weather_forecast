import numpy as np
import vtk



def main():
    cols = vtk.vtkNamedColors()
    cols.SetColor("lightbrown", [77, 51, 26, 255])
    cols.SetColor("man", [255, 255, 0, 255])

    reader_house = vtk.vtkOBJReader()
    reader_house.SetFileName("house.obj")


    mapper_house = vtk.vtkPolyDataMapper()
    mapper_house.SetInputConnection(reader_house.GetOutputPort())


    actor_house = vtk.vtkActor()
    actor_house.SetMapper(mapper_house)
    actor_house.GetProperty().SetColor(cols.GetColor3d("lightbrown"))


    reader_legoman = vtk.vtkOBJReader()
    reader_legoman.SetFileName("lego_man.obj")


    trans = vtk.vtkTransform()
    trans.Scale(10, 10, 10)
    trans.Translate(-17, 0, -1)
    trans.RotateY(-90)

    transFilter = vtk.vtkTransformPolyDataFilter()
    transFilter.SetInputConnection(reader_legoman.GetOutputPort())
    transFilter.SetTransform(trans)
    transFilter.Update()


    mapper_legoman = vtk.vtkPolyDataMapper()
    mapper_legoman.SetInputConnection(transFilter.GetOutputPort())



    actor_legoman = vtk.vtkActor()
    actor_legoman.SetMapper(mapper_legoman)
    actor_legoman.GetProperty().SetColor(cols.GetColor3d("man"))



    renderer = vtk.vtkRenderer()




    rendererWindow= vtk.vtkRenderWindow()
    rendererWindow.AddRenderer(renderer)
    rendererWindow.SetSize(1024, 768)


    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(rendererWindow)

    intStyle = vtk.vtkInteractorStyleTrackballCamera()
    interactor.SetInteractorStyle(intStyle)


    renderer.AddActor(actor_house)
    renderer.AddActor(actor_legoman)


    rendererWindow.Render()

    interactor.Start()

if __name__ == "__main__":
    main()