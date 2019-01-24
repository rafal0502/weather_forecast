import vtk


def prec_actor(x, y, prec):

    cube_source = vtk.vtkCubeSource()
    cube_source.SetXLength(7)
    cube_source.SetYLength(7)
    height = prec * 50
    cube_source.SetZLength(height)
    cube_source.SetCenter(x, y, height / 2)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cube_source.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0, 255, 0)
    actor.SetVisibility(True)

    return actor
