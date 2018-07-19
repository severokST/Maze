from config import UI
from pyglet import window, app, graphics, clock, gl
from pyglet.window import key
from Models import map_node, wall, actor, player, enemy, object_key, object_door
from random import choice

main_window = window.Window(width=UI['Main']['size'][0], height=UI['Main']['size'][1])

keys = key.KeyStateHandler()
main_window.push_handlers(keys)


class Level:
    def __init__(self):
        self.level = 1
        self.player = None
        self.map_nodes = {}
        self.object_list = []
        self.npc_list = []
        self.map_objects = []
        self.generate_level()

    def level_up(self):
        self.level +=1
        self.generate_level()

    def restart(self):
        self.level = 0
        self.generate_level()

    def clean_up(self):
        self.map_nodes.clear()
        self.object_list.clear()
        self.npc_list.clear()
        self.map_objects.clear()

    def generate_level(self):
        self.clean_up()
        tile_count = 50 + self.level * 10
        enemy_count = int(self.level) + 1
        self.map_nodes = map_node.new_map(tile_count)
        self.map_objects = wall.generate_walls(self.map_nodes)

        for count in range(0, enemy_count):
            self.npc_list.append(enemy.Enemy(choice(list(self.map_nodes))))

        self.object_list.append(object_key.key(choice(list(self.map_nodes))))
        self.player = player.PC(choice(list(self.map_nodes)))

        print(self.player.position)

        for attempts in range(0, 100):
            potential_exit = self.map_nodes[choice(list(self.map_nodes))]
            if len(potential_exit.links) == 1 or attempts == 100:
                self.object_list.append(object_door.door(potential_exit.position))
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
        level.player.key(keys, level.map_nodes)
        level.player.update()
        for enemy in level.npc_list:
            if enemy.decision(level.player, level.map_nodes) == 'hit':
                print('Hit')
                level.restart()
            enemy.update()
        for item in range(len(level.object_list)-1,-1,-1):
            event = level.object_list[item].collision(level.player)
            if event == 'item_get':
                del level.object_list[item]
            if event == 'use_door':
                level.level_up()


level = Level()

clock.schedule_interval(update,1/30);

app.run()

