import pyglet
from graphics.button import Button


class GameWindow(pyglet.window.Window):
    def __init__(self, title='Game', width=720, height=400, x=100, y=100):
        super(GameWindow, self).__init__()
        # window
        self.set_location(x, y)
        self.set_size(width, height)
        self.set_caption(title)
        # variables
        self.objects = list()
        self.keys = dict()


    def on_draw(self):
        self.clear()
        for obj in self.objects:
            obj.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        for obj in self.objects:
            if obj.type == 'BUTTON':
                if obj.pos[0] < x < obj.size[0]:
                    if obj.pos[1] < y < (obj.size[1] + obj.size[1]):
                        obj.function()


    def on_key_press(self, symbol, modifiers):
        keys = pyglet.window.key
        if symbol == keys.ESCAPE:
            pyglet.app.exit()


    def addObject(self, obj):
        self.objects.append(obj)


    def run(self):
        pyglet.app.run()


if __name__ == '__main__':
    b = Button(20, 20, 100, 40, "Test")
    w = GameWindow()
    w.addObject(b)
    w.run()