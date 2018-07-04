from pyglet import sprite, image
from config import UI


x_y = [0, 1]

# Generic actor class, simple moveable object in maz
images = {'Generic': image.load('./images/generic.png'),
          'Player': image.load('./images/player.png'),
          'Enemy': image.load('./images/enemy.png'),}


class Actor:
    def __init__(self, position):
        self.image_reference = 0
        self.position = position
        self.target_position = position
        self.speed = 1
        self.attributes = ()
        self.render_position = tuple(map(lambda x: UI['Field']['position'][x] +
                                                   (UI['Field']['size'][x] / UI['grid_size'][x]) * self.position[x], x_y))
        self.target_render_position = self.render_position
        self.sprite = sprite.Sprite(images['Player'], batch=UI['batch_map'], group=UI['background'],
                                    x=self.render_position[0], y=self.render_position[1])

    def move(self, direction, map_node):
        # Reject command if actor has not yet completed previous move
        if self.position == self.target_position and direction in map_node[self.position].links:
            delta = {'up': (0, 1), 'down': (0, -1), 'left': (-1, 0), 'right': (1, 0),
                     'up-left': (1, 1), 'down-left': (-1, -1),
                     'up-right': (1, 1), 'down-right': (-1, 1)}
            self.target_position = tuple(map(lambda x: self.position[x] + delta[direction][x], x_y))
            self.target_render_position = tuple(map(lambda x: UI['Field']['position'][x] +
                                                              (UI['Field']['size'][x] / UI['grid_size'][x]) *
                                                              self.target_position[x], x_y))

    def update(self):

        if self.position != self.target_position:

            self.sprite.position = tuple(map(lambda x: self.sprite.position[x]
                                                - sorted((-1*self.speed,(self.sprite.position[x]
                                                - self.target_render_position[x]),self.speed))[1], x_y))

            if self.sprite.position == self.target_render_position:
                self.position = self.target_position





