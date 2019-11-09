from turtle_drawer import TurtleDrawer
from turtle_lib import TurtleDrawerLib


class GraphicalAdapter(TurtleDrawer, TurtleDrawerLib):
    def __init__(self, drawer):
        self.drawer = drawer

    def pen_down(self):
        self.drawer.pen_down()

    def pen_up(self):
        self.drawer.pen_up()

    def go_along(self, along):
        self.drawer.go_along(along)

    def go_down(self, down):
        self.drawer.go_down(down)

    def draw_circle(self, radius):
        self.drawer.draw_circle(radius)

    def draw_triangle(self, size):
        self.drawer.draw_triangle(size)

