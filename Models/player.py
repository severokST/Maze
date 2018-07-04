from Models import actor
from pyglet.window import key
from Models.actor import images


class PC(actor.Actor):
    def __init__(self, position):
        actor.Actor.__init__(self, position)
        self.speed = 2
        self.sprite.image = images['Player']
        self.inv = ()

    def die(self):
        print('Splat')
        #self.sprite.delete()
        del self

    def key(self, keys, map_nodes):
        if keys[key.MOTION_RIGHT]:
            self.move('right', map_nodes)
        if keys[key.MOTION_LEFT]:
            self.move('left', map_nodes)
        if keys[key.MOTION_UP]:
            self.move('up', map_nodes)
        if keys[key.MOTION_DOWN]:
            self.move('down', map_nodes)