import vtk


def cloud_actor(x, y,  clouds):
    cloud_source = vtk.vtkSTLReader()
    cloud_source.SetFileName("images/cloud.stl")

    translation = vtk.vtkTransform()
    translation.Translate(x, y, 40)
    translation.Scale(clouds / 10, clouds / 10, clouds / 10)

    transform_filter = vtk.vtkTransformPolyDataFilter()
    transform_filter.SetTransform(translation)
    transform_filter.SetInputConnection(cloud_source.GetOutputPort())

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(transform_filter.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.SetVisibility(True)

    return actor
