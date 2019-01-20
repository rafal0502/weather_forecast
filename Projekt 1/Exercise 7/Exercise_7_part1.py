import numpy as np
import vtk
import time

def main():
    cubeSource = vtk.vtkCubeSource()
    cubeSource.SetCenter(0, 0, 0)
    cubeSource.SetXLength(2.5)
    cubeSource.SetYLength(3.5)
    cubeSource.SetZLength(4.5)


    # Create a mapper and actor
    mapper_1 = vtk.vtkPolyDataMapper()
    mapper_1.SetInputConnection(cubeSource.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper_1)
    actor.GetProperty().SetColor(255, 0, 0)


    cubeSource_2 = vtk.vtkCubeSource()
    cubeSource_2.SetCenter(0, 10, 0)
    cubeSource_2.SetXLength(2.5)
    cubeSource_2.SetYLength(3.5)
    cubeSource_2.SetZLength(4.5)


    mapper_2 = vtk.vtkPolyDataMapper()
    mapper_2.SetInputConnection(cubeSource_2.GetOutputPort())


    actor_2 = vtk.vtkActor()
    actor_2.SetMapper(mapper_2)
    actor_2.GetProperty().SetColor(0, 255, 0)




    cubeSource_3 = vtk.vtkCubeSource()
    cubeSource_3.SetCenter(10, 0, 0)
    cubeSource_3.SetXLength(2.5)
    cubeSource_3.SetYLength(3.5)
    cubeSource_3.SetZLength(4.5)


    mapper_3 = vtk.vtkPolyDataMapper()
    mapper_3.SetInputConnection(cubeSource_3.GetOutputPort())

    actor_3 = vtk.vtkActor()
    actor_3.SetMapper(mapper_3)
    actor_3.GetProperty().SetColor(0, 0, 255)




    cubeSource_4 = vtk.vtkCubeSource()
    cubeSource_4.SetCenter(10, 10, 0)
    cubeSource_4.SetXLength(2.5)
    cubeSource_4.SetYLength(3.5)
    cubeSource_4.SetZLength(4.5)



    mapper_4 = vtk.vtkPolyDataMapper()
    mapper_4.SetInputConnection(cubeSource_4.GetOutputPort())


    actor_4 = vtk.vtkActor()
    actor_4.SetMapper(mapper_4)
    actor_4.GetProperty().SetColor(255, 255, 0)


    # Add lights
    light = vtk.vtkLight()
    light.SetLightTypeToSceneLight()
    light.SetColor(255, 255, 255)

    light_2 = vtk.vtkLight()
    light.SetLightTypeToSceneLight()
    light.SetColor(0, 0, 255)

    light_3 = vtk.vtkLight()
    light.SetLightTypeToSceneLight()
    light.SetColor(255, 0, 0)



    #Visualize
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.AddActor(actor_2)
    renderer.AddActor(actor_3)
    renderer.AddActor(actor_4)
    renderer.AddLight(light)
    renderer.AddLight(light_2)
    renderer.AddLight(light_3)


    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)



    interactor = vtk.vtkRenderWindowInteractor()


    interactor.SetRenderWindow(renderWindow)
    istyle = vtk.vtkInteractorStyleSwitch()
    interactor.SetInteractorStyle(istyle)
    istyle.SetCurrentStyleToTrackballCamera()


    interactor.Initialize()
    interactor.Start()

if __name__ == "__main__":
    main()