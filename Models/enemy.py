from Models import actor
from math import pow, sqrt
from random import choice
from Models.actor import images


class Enemy(actor.Actor):
    def __init__(self, position):
        actor.Actor.__init__(self, position)
        self.speed = 1.2
        self.sprite.image = images['Enemy']

    def decision(self, player, map_nodes):
        dx = player.sprite.position[0] - self.sprite.position[0]
        dy = player.sprite.position[1] - self.sprite.position[1]
        distance_from_player = int(sqrt(pow(dx, 2) +
                                        pow(dy, 2)))

        if distance_from_player < 2:
            player.die()

        if self.position == self.target_position:

            direction_choice = 'none'
            if distance_from_player <= 100:
                if dx > 0 and 'right' in map_nodes[self.position].links:
                    direction_choice = 'right'
                if dx < 0 and 'left' in map_nodes[self.position].links:
                    direction_choice = 'left'
                if dy > 0 and 'up' in map_nodes[self.position].links:
                    direction_choice = 'up'
                if dy < 0 and 'down' in map_nodes[self.position].links:
                    direction_choice = 'down'
            if direction_choice == 'none':
                direction_choice = choice(list(map_nodes[self.position].links))

            if direction_choice in ('up', 'down', 'left', 'right'):
                self.move(direction_choice, map_nodes)


