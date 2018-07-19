from Models import actor
from Models.actor import images


class door(actor.Actor):
    def __init__(self, position):
        actor.Actor.__init__(self, position)
        self.sprite.image = images['Door']

    def update(self):
        pass

    def collision(self, player):
        if player.position == self.position:
            if 'key' in player.inv:
                return 'use_door'

