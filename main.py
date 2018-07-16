from config import UI
from pyglet import window, app, graphics, clock, gl
from pyglet.window import key
from Models import map_node, wall, actor, player, enemy, object_key, object_door
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

object_list.append(object_key.key(choice(list(map_nodes))))

for attempts in range(0,100):
    potential_exit = map_nodes[choice(list(map_nodes))]
    if len(potential_exit.links) == 1 or attempts == 100:
        object_list.append(object_door.door(potential_exit.position))
        break


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
    for item in range(0, len(object_list)):
        if object_list[item].collision(player) == 1:
            del object_list[item]






clock.schedule_interval(update,1/30);

app.run()

