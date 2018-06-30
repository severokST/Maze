from pyglet import image, sprite, graphics, gl


images = [image.load('./images/wall.png')]

time_scale = 1


class Wall:
    def __init__(self, ui, position):
        self.position = position
        self.sprite = sprite.Sprite(images[0], batch=ui['batch_map'], group=ui['background'],
                                x=self.position[0], y=self.position[1])


# V0 - Read though all avalaible nodes and connection references. Place walls where ever no connection exists
#   Todo: All walls appear to be genrated -90 degrees from correct orientation. Investigate and fix.

def generate_walls(UI, map_nodes):
    map_walls = []
    grid_resolution = UI['Field']['size'][0] / UI['grid_size'][0], UI['Field']['size'][1] / UI['grid_size'][1]
    position_offset = grid_resolution[0]/6, grid_resolution[1]/6
    for node in map_nodes:
        print (node, map_nodes[node].links)
        node_position = UI['Field']['position'][0] + map_nodes[node].position[0] * grid_resolution[0], \
                        UI['Field']['position'][1] + map_nodes[node].position[1] * grid_resolution[1]
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
            map_walls.append(Wall(UI, (node_position[0] - position_offset[0], node_position[1]- position_offset[1])))
        if 'down-right' not in map_nodes[node].links:
            map_walls.append(Wall(UI, (node_position[0] + position_offset[0], node_position[1] - position_offset[1])))

    return map_walls