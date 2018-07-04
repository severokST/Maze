from pyglet import graphics

UI = {
        'Main': {'size': [800, 600],   'position': [0, 0]},
        'Field': {'size': [700, 500],  'position': [50, 50]},
        'grid_size': [35,25],
        'batch_actors': graphics.Batch(),
        'batch_map': graphics.Batch(),
        'foreground': graphics.OrderedGroup(1),
        'background': graphics.OrderedGroup(2)
}
