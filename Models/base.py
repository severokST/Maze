from pyglet import sprite

import types

class Basic:
    def __init__(self, name, batch, group, position):
        self.name = name
        self.position = position
        self.visible = False
        self.sprite = sprite.Sprite(None, batch=batch, group=group, x=position[0], y=position[1])

    def set_visible(self,value):
        #self.sprite.visible = value
        pass

    def set_position(self,value):
        self.position = value

    def __del__(self):
        #self.sprite.delete()
        pass



