import pyglet


class Button:
    def __init__(self, x, y, width, height, title, function=lambda: print("Button Test")):
        self.pos = [x, y]
        self.size = [width, height]
        self.title = title
        self.function = function
        self.type = 'BUTTON'
        self.button = pyglet.shapes.Rectangle(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.text = pyglet.text.Label(text=self.title, font_name='consolas', font_size=22)
        dx = (self.pos[0] + self.size[0]//2) - self.text.content_width//2
        dy = (self.pos[1] + self.size[1]//2) - self.text.content_height//2 + 5
        self.text.x = dx
        self.text.y = dy
        self.text.color = (0, 0, 0, 255)


    def draw(self):
        self.button.draw()
        self.text.draw()


    def getFunction(self):
        return self.function