from pyglet import sprite, image
from pyglet.window import key
from math import sin,cos,tan

x_y = [0, 1]

# Generic actor class, simple moveable object in maz
images = {'Generic': image.load('./images/generic.png'),
          'Player': image.load('./images/player.png'),
          'Enemy': image.load('./images/enemy.png'),}


class Actor:
    def __init__(self, ui, position):
        self.image_reference = 0
        self.position = position
        self.target_position = position
        self.speed = 1
        self.attributes = ()
        self.render_position = tuple(map(lambda x: ui['Field']['size'][x] / ui['grid_size'][x] * self.position[x], x_y))
        self.sprite = sprite.Sprite(images['Player'], batch=ui['batch_map'], group=ui['background'],
                                    x=self.render_position[0], y=self.render_position[1])

    def move(self, direction, map_node):
        # Reject command if actor has not yet completed previous move
        if self.position == self.target_position and direction in map_node[self.position].links:
            delta = {'up': (0, 1), 'down': (0, -1), 'left': (-1, 0), 'right': (1, 0)}
            self.target_position =  tuple(map(lambda x: self.position[x] + delta[direction][x], x_y))
            print(self.target_position)

    def update(self, ui):
        self.position = self.target_position
        self.sprite.position = tuple(map(lambda x: (ui['Field']['size'][x] / ui['grid_size'][x])  * self.position[x] , x_y))



class PC(Actor):
    def key(self, keys, node_map):
        if keys[key.MOTION_RIGHT]:
            print('Right')
            self.move('right', node_map)
        if keys[key.MOTION_LEFT]:
            print('Left')
            self.move('left', node_map)
        if keys[key.MOTION_UP]:
            self.move('up', node_map)
        if keys[key.MOTION_DOWN]:
            self.move('down' ,node_map)