from pyglet import window, app, graphics, clock, gl
from pyglet.window import key
from Models import map_node, wall, actor
from random import choice
import random


UI = {
        'Main': {'size': [800, 600],   'position': [0, 0]},
        'Field': {'size': [700, 500],  'position': [50, 50]},
        'grid_size': [35,25],
        'batch_actors': graphics.Batch(),
        'batch_map': graphics.Batch(),
        'foreground': graphics.OrderedGroup(1),
        'background': graphics.OrderedGroup(2)
}


main_window = window.Window(width=UI['Main']['size'][0], height=UI['Main']['size'][1])

keys = key.KeyStateHandler()
main_window.push_handlers(keys)

map_nodes = map_node.new_map(200, UI['grid_size'])
map_objects = wall.generate_walls(UI, map_nodes)
player = actor.PC(UI, choice(list(map_nodes)))
object_list = []

@main_window.event
def on_draw():
    main_window.clear()
    UI['batch_actors'].draw()
    UI['batch_map'].draw()
    graphics.draw(4, gl.GL_LINE_LOOP, ('v2i', [
        UI['Field']['position'][0], UI['Field']['position'][1],
        UI['Field']['position'][0]+UI['Field']['size'][0], UI['Field']['position'][1],
        UI['Field']['position'][0]+UI['Field']['size'][0], UI['Field']['position'][1]+UI['Field']['size'][1],
        UI['Field']['position'][0], UI['Field']['position'][1]+UI['Field']['size'][1],
    ]))


def update(dt):
    player.key(keys, map_nodes, UI)
    player.update()
    for obj in object_list:
        pass








clock.schedule_interval(update,1/30);

app.run()

