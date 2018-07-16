from Models import actor
from math import pow, sqrt
from random import choice
from Models.actor import images


class Enemy(actor.Actor):
    def __init__(self, position):
        actor.Actor.__init__(self, position)
        self.speed = 2
        self.sprite.image = images['Enemy']

    def path_find_player(self, player, map_nodes):
        next_location = {'up': (0, 1), 'down': (0, -1), 'left': (-1, 0), 'right': (1, 0)}
        checked_node = set()
        check_list = []

        for initial in map_nodes[self.position].links:
            if initial in next_location.keys():
                connecting_location = (self.position[0] + next_location[initial][0], self.position[1] + next_location[initial][1])
                if connecting_location == player.position:
                    return initial
                check_list.append({'initial_direction': initial, 'location':connecting_location, 'distance': 1})
                checked_node.add(self.position)


        while True:
            target_location = check_list[0]
            del check_list[0]
            target_distance = target_location['distance'] + 1

            # Escape seeking if player has not been reached within 10 steps, no pathing solution found
            if target_distance > 10:
                return 'none'

            for connecting_direction in map_nodes[target_location['location']].links:
                if connecting_direction in next_location.keys():
                    connecting_location = (target_location['location'][0] + next_location[connecting_direction][0],
                                           target_location['location'][1] + next_location[connecting_direction][1])
                    if connecting_location == player.position:
                        return target_location['initial_direction']
                    if connecting_location not in checked_node:
                        check_list.append({'initial_direction': target_location['initial_direction'],
                                           'location': connecting_location, 'distance': target_distance})
                        checked_node.add(target_location['location'])




    def decision(self, player, map_nodes):
        dx_grid = player.position[0] - self.position[0]
        dy_grid = player.position[1] - self.position[1]
        distance_from_player_grid = int(sqrt(pow(dx_grid,2)+pow(dy_grid,2)))

        dx = player.sprite.position[0] - self.sprite.position[0]
        dy = player.sprite.position[1] - self.sprite.position[1]
        distance_from_player = int(sqrt(pow(dx, 2) +
                                        pow(dy, 2)))

        if distance_from_player < 2:
            player.die()

        if self.position == self.target_position:
            direction_choice = 'none'
            if distance_from_player_grid < 5:
                direction_choice = self.path_find_player(player, map_nodes)

            if direction_choice == 'none':
                direction_choice = choice(list(map_nodes[self.position].links))

            if direction_choice in ('up', 'down', 'left', 'right'):
                self.move(direction_choice, map_nodes)


