from pyglet import image, sprite, graphics, gl
from config import UI

x_y = [0, 1]
images = [image.load('./images/wall.png')]
time_scale = 1


class Wall:
    def __init__(self, ui, position):
        self.position = position
        self.sprite = sprite.Sprite(images[0], batch=ui['batch_map'], group=ui['background'],
                                    x=self.position[0], y=self.position[1])


# V0 - Read though all avalaible nodes and connection references. Place walls where ever no connection exists
#   Todo: All walls appear to be genrated -90 degrees from correct orientation. Investigate and fix.
#       Appears to be due to Pyglet co-ordinates originating Lower-left instead of upper left.
#   Todo: Re-check logic for Y-axis references. Likely applying incorrect neighbour link flags.

def generate_walls(map_nodes):
    map_walls = []

    grid_resolution = tuple(map(lambda x: UI['Field']['size'][x] / UI['grid_size'][x], x_y))
    position_offset = tuple(map(lambda x: grid_resolution[x]/3, x_y))

    for node in map_nodes:
        print (node, map_nodes[node].links)

        node_position = tuple(map(lambda x: UI['Field']['position'][x] +
                                            map_nodes[node].position[x] * grid_resolution[x], x_y))

        if 'up' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0], node_position[1] + position_offset[1])))
        if 'down' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0], node_position[1] - position_offset[1])))
        if 'left' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0] - position_offset[0], node_position[1])))
        if 'right' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0] + position_offset[0], node_position[1])))
        if 'up-left' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0] - position_offset[0], node_position[1] + position_offset[1])))
        if 'up-right' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0] + position_offset[0], node_position[1] + position_offset[1])))
        if 'down-left' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0] - position_offset[0], node_position[1] - position_offset[1])))
        if 'down-right' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0] + position_offset[0], node_position[1] - position_offset[1])))

    return map_walls

