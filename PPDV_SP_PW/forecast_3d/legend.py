import vtk

tem_col = vtk.vtkNamedColors()
for i in range(0, 11):
    tem_col.SetColor('<' + str(-20+i*5), [i * 20, 100, 255 - i * 20, 255])
tem_col.SetColor('>=' + str(30), [255, 100, 0, 255])

p_col = vtk.vtkNamedColors()
for i in range(0, 11):
    p_col.SetColor('<' + str(950+i*10), [i * 20, 255 - i * 20, 100, 255])
p_col.SetColor('>=' + str(1050), [255, 0, 100, 255])


def legend_actor(wgt_width, wgt_height):
    legend_actors = []

    temperature_item_height = wgt_height / 20
    temperature_item_width = 60
    p_item_height = wgt_height / 20
    p_item_width = 60

    for i in range(0, 11):
        temp_cube_source = vtk.vtkCubeSource()
        temp_cube_source.SetXLength(temperature_item_width)
        temp_cube_source.SetYLength(temperature_item_height)
        temp_cube_source.SetCenter(wgt_width - (temperature_item_width / 2),
                                   temperature_item_height / 2 + i * temperature_item_height, 0)

        mapper = vtk.vtkPolyDataMapper2D()
        mapper.SetInputConnection(temp_cube_source.GetOutputPort())

        actor = vtk.vtkActor2D()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(tem_col.GetColor3d('<' + str(-20 + i*5)))

        legend_actors.append(actor)

        txt = vtk.vtkTextActor()
        txt.SetInput('<' + str(-20 + i * 5))
        txt.GetTextProperty().SetFontFamilyToTimes()
        txt.GetTextProperty().SetFontSize(18)
        txt.GetTextProperty().SetColor(0, 0, 0)
        txt.SetDisplayPosition(int(wgt_width - (temperature_item_width / 2) - 20),
                               int((temperature_item_height / 2) + (i * temperature_item_height) - 12))

        legend_actors.append(txt)

    temp_cube_source = vtk.vtkCubeSource()
    temp_cube_source.SetXLength(temperature_item_width)
    temp_cube_source.SetYLength(temperature_item_height)
    temp_cube_source.SetCenter(wgt_width - (temperature_item_width / 2),
                               temperature_item_height / 2 + 11 * temperature_item_height, 0)

    mapper = vtk.vtkPolyDataMapper2D()
    mapper.SetInputConnection(temp_cube_source.GetOutputPort())

    actor = vtk.vtkActor2D()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(tem_col.GetColor3d('>=30'))

    legend_actors.append(actor)

    cube_source = vtk.vtkCubeSource()
    cube_source.SetXLength(temperature_item_width)
    cube_source.SetYLength(temperature_item_height)
    cube_source.SetCenter(wgt_width - (temperature_item_width / 2),
                          temperature_item_height / 2 + 12 * temperature_item_height,
                          0)

    mapper = vtk.vtkPolyDataMapper2D()
    mapper.SetInputConnection(cube_source.GetOutputPort())

    actor = vtk.vtkActor2D()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.1, 0.1, 0.1)

    legend_actors.append(actor)

    txt = vtk.vtkTextActor()
    txt.SetInput("T [ºC]")
    txt.GetTextProperty().SetFontFamilyToTimes()
    txt.GetTextProperty().SetFontSize(18)
    txt.GetTextProperty().SetColor(1, 1, 1)
    txt.SetDisplayPosition(int(wgt_width - (temperature_item_width / 2) - 25),
                           int(temperature_item_height / 2 + 12 * temperature_item_height - 12))

    legend_actors.append(txt)

    txt = vtk.vtkTextActor()
    txt.SetInput('>=' + str(30))
    txt.GetTextProperty().SetFontFamilyToTimes()
    txt.GetTextProperty().SetFontSize(18)
    txt.GetTextProperty().SetColor(0, 0, 0)
    txt.SetDisplayPosition(int(wgt_width - (temperature_item_width / 2) - 25),
                           int((temperature_item_height / 2) + (11 * temperature_item_height) - 12))

    legend_actors.append(txt)

    for i in range(0, 11):
        p_cube_source = vtk.vtkCubeSource()
        p_cube_source.SetXLength(p_item_width)
        p_cube_source.SetYLength(p_item_height)
        p_cube_source.SetCenter((p_item_width / 2),
                                   p_item_height / 2 + i * p_item_height, 0)

        mapper = vtk.vtkPolyDataMapper2D()
        mapper.SetInputConnection(p_cube_source.GetOutputPort())

        actor = vtk.vtkActor2D()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(p_col.GetColor3d('<' + str(950 + i * 10)))

        legend_actors.append(actor)

        txt = vtk.vtkTextActor()
        txt.SetInput('<' + str(950 + i * 10))
        txt.GetTextProperty().SetFontFamilyToTimes()
        txt.GetTextProperty().SetFontSize(18)
        txt.GetTextProperty().SetColor(0, 0, 0)
        txt.SetDisplayPosition(int((p_item_width / 2) - 30),
                               int((p_item_height / 2) + (i * p_item_height) - 12))

        legend_actors.append(txt)

    p_cube_source = vtk.vtkCubeSource()
    p_cube_source.SetXLength(p_item_width)
    p_cube_source.SetYLength(p_item_height)
    p_cube_source.SetCenter((p_item_width / 2),
                            p_item_height / 2 + 11 * p_item_height, 0)

    mapper = vtk.vtkPolyDataMapper2D()
    mapper.SetInputConnection(p_cube_source.GetOutputPort())

    actor = vtk.vtkActor2D()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(p_col.GetColor3d('>=1050'))

    legend_actors.append(actor)

    txt = vtk.vtkTextActor()
    txt.SetInput('>' + str(1050))
    txt.GetTextProperty().SetFontFamilyToTimes()
    txt.GetTextProperty().SetFontSize(18)
    txt.GetTextProperty().SetColor(0, 0, 0)
    txt.SetDisplayPosition(int((p_item_width / 2) - 30),
                           int((p_item_height / 2) + (11 * p_item_height) - 12))

    legend_actors.append(txt)

    p_cube_source = vtk.vtkCubeSource()
    p_cube_source.SetXLength(p_item_width)
    p_cube_source.SetYLength(p_item_height)
    p_cube_source.SetCenter((p_item_width / 2),
                            p_item_height / 2 + 12 * p_item_height, 0)

    mapper = vtk.vtkPolyDataMapper2D()
    mapper.SetInputConnection(p_cube_source.GetOutputPort())

    actor = vtk.vtkActor2D()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.1, 0.1, 0.1)
    legend_actors.append(actor)

    txt = vtk.vtkTextActor()
    txt.SetInput("p [hPa]")
    txt.GetTextProperty().SetFontFamilyToTimes()
    txt.GetTextProperty().SetFontSize(18)
    txt.GetTextProperty().SetColor(1, 1, 1)
    txt.SetDisplayPosition(int(p_item_width / 2 - 29),
                           int(p_item_height / 2 + 12 * p_item_height - 12))

    legend_actors.append(txt)

    return legend_actors
