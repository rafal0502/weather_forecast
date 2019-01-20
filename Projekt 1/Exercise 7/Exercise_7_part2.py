import vtk


def main():
    points = vtk.vtkPoints()
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(10, 0, 0)
    points.InsertNextPoint(0, 10, 0)
    points.InsertNextPoint(10, 10, 0)

    grid = vtk.vtkPolyData()
    grid.SetPoints(points)

    cube = vtk.vtkCubeSource()

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    colors = vtk.vtkUnsignedCharArray()
    colors.SetNumberOfComponents(3)
    colors.SetName("colors")
    colors.InsertNextTuple(red)
    colors.InsertNextTuple(green)
    colors.InsertNextTuple(blue)
    colors.InsertNextTuple(yellow)

    grid.GetPointData().SetScalars(colors)

    filter = vtk.vtkGlyph3D()
    filter.SetSourceConnection(cube.GetOutputPort())
    filter.SetScaleModeToDataScalingOff()
    filter.SetColorModeToColorByScalar()
    filter.SetInputData(grid)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(filter.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetPointSize(5)

    rend = vtk.vtkRenderer()
    rend.AddActor(actor)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(rend)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    renderWindow.Render()
    interactor.Start()


if __name__ == "__main__":
    main()
