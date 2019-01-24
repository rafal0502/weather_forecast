import vtk


def temperature_actor(x, y, temp, col):
    cube_source = vtk.vtkCubeSource()
    cube_source.SetXLength(30)
    cube_source.SetYLength(30)
    cube_source.SetZLength(1)
    cube_source.SetCenter(x, y - 19, 0)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cube_source.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(col)
    actor.SetVisibility(True)

    atext = vtk.vtkVectorText()
    atext.SetText("{:.0f}".format(temp).center(4))
    textMapper = vtk.vtkPolyDataMapper()
    textMapper.SetInputConnection(atext.GetOutputPort())
    textActor = vtk.vtkFollower()
    textActor.SetMapper(textMapper)
    textActor.SetScale(8, 8, 8)
    textActor.AddPosition(x - 15, y - 23, 1)
    textActor.GetProperty().SetColor(1, 1, 1)
    textActor.SetVisibility(True)

    return actor, textActor
