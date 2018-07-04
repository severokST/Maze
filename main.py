from config import UI
from pyglet import window, app, graphics, clock, gl
from pyglet.window import key
from Models import map_node, wall, actor, player, enemy
from random import choice




main_window = window.Window(width=UI['Main']['size'][0], height=UI['Main']['size'][1])

keys = key.KeyStateHandler()
main_window.push_handlers(keys)

map_nodes = map_node.new_map(200)
map_objects = wall.generate_walls(map_nodes)
player = player.PC(choice(list(map_nodes)))



object_list = []
npc_list = []

for i in range(0, 3):
    npc_list.append(enemy.Enemy(choice(list(map_nodes))))




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
    player.key(keys, map_nodes)
    player.update()
    for enemy in npc_list:
        enemy.decision(player, map_nodes)
        enemy.update()








clock.schedule_interval(update,1/30);

app.run()

