from math import sin, radians, cos

import vtk


def wind_actor(x, y, speed, deg):
    arrow_length = speed * 10

    arrow_source = vtk.vtkArrowSource()
    arrow_source.SetShaftResolution(50)
    arrow_source.SetTipResolution(50)

    start_point = [x, y, 25]
    end_point = [x - arrow_length * sin(radians(deg)), y - arrow_length * cos(radians(deg)), 25]

    normalizedX = [0 for i in range(3)]
    normalizedY = [0 for i in range(3)]
    normalizedZ = [0 for i in range(3)]

    # The X axis is a vector from start to end
    math = vtk.vtkMath()
    math.Subtract(end_point, start_point, normalizedX)
    length = math.Norm(normalizedX)
    math.Normalize(normalizedX)

    # The Z axis is an arbitrary vector cross X
    arbitrary = [0 for i in range(3)]
    arbitrary[0] = 1
    arbitrary[1] = 1
    arbitrary[2] = 1
    math.Cross(normalizedX, arbitrary, normalizedZ)
    math.Normalize(normalizedZ)

    # The Y axis is Z cross X
    math.Cross(normalizedZ, normalizedX, normalizedY)
    matrix = vtk.vtkMatrix4x4()

    # Create the direction cosine matrix
    matrix.Identity()
    for i in range(3):
        matrix.SetElement(i, 0, normalizedX[i])
        matrix.SetElement(i, 1, normalizedY[i])
        matrix.SetElement(i, 2, normalizedZ[i])

    transform = vtk.vtkTransform()
    transform.Translate(start_point)
    transform.Concatenate(matrix)
    transform.Scale(length, length, length)

    transform_filter = vtk.vtkTransformPolyDataFilter()
    transform_filter.SetTransform(transform)
    transform_filter.SetInputConnection(arrow_source.GetOutputPort())

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(transform_filter.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(255, 0, 0)
    actor.SetVisibility(True)

    return actor
