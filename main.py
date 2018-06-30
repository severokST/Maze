from pyglet import window, app, graphics, clock,gl
from Models import map_node, wall
import random


UI = {
        'Main': {'size': [800, 600],   'position': [0, 0]},
        'Field': {'size': [500, 500],  'position': [50, 50]},
        'grid_size': [20,20],
        'batch_actors': graphics.Batch(),
        'batch_map': graphics.Batch(),
        'foreground': graphics.OrderedGroup(1),
        'background': graphics.OrderedGroup(2)
}

#UI['Grid']['step'] = [UI['Field']['size'][0] / UI['Grid']['resolution'][0],
#                      UI['Field']['size'][1] / UI['Grid']['resolution'][1]]

main_window = window.Window(width=UI['Main']['size'][0], height=UI['Main']['size'][1])

map_nodes = map_node.new_map(100, UI['grid_size'])
map_objects = wall.generate_walls(UI,map_nodes)


object_list = []

@main_window.event
def on_draw():
    #main_window.clear()
    UI['batch_actors'].draw()
    UI['batch_map'].draw()
    graphics.draw(4,gl.GL_LINE_LOOP,('v2i',[
        UI['Field']['position'][0], UI['Field']['position'][1],
        UI['Field']['position'][0]+UI['Field']['size'][0], UI['Field']['position'][1],
        UI['Field']['position'][0]+UI['Field']['size'][0], UI['Field']['position'][1]+UI['Field']['size'][1],
        UI['Field']['position'][0], UI['Field']['position'][1]+UI['Field']['size'][1],
    ]))


def update(dt):
    for obj in object_list:
        pass








clock.schedule_interval(update,1/30);

app.run()

