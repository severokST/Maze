from Models import actor
from Models.actor import images

class key(actor.Actor):
    def __init__(self, position):
        actor.Actor.__init__(self, position)
        self.sprite.image = images['Key']

    def update(self):
        pass

    def collision(self, player):
        if player.position == self.position:
            player.inv.add('key')
            print('player inv:', player.inv)
            return 1
        return 0