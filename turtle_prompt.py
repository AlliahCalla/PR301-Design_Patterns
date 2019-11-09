from turtle_drawer import TurtleDrawer
from cmd import Cmd
from writer import *
from tigr import AbstractParser
from turtle_lib import TurtleDrawerLib
from graphics_adapter import GraphicalAdapter


class TurtlePrompt(Cmd, AbstractParser):
    results = Writer("TurtleDrawer_Result.txt")
    welcome = "Welcome to Turtle Shell"
    prompt = '(turtle)'
    file = None


    def parse(self, raw_source):
        self.source = raw_source
        try:
            self.data = int(self.source)
        except:
            self.command = str(self.source)

    def do_P(self, arg):
        """Select Pen:  P 10"""
        self.results.writeToFile("Selected pen", arg)
        self.parse(arg)
        turtle_drawer = TurtleDrawer()
        turtle_drawer.select_pen(self.data)

    def do_U(self, arg):
        """Pen Up : U"""
        self.results.writeToFile("Pen is up", arg)
        self.parse(arg)
        turtle_lib = TurtleDrawerLib()
        adapter = GraphicalAdapter(turtle_lib)
        adapter.pen_up()

    def do_D(self, arg):
        """Pen Down : D"""
        self.results.writeToFile("Pen is down", arg)
        self.parse(arg)
        turtle_lib = TurtleDrawerLib()
        adapter = GraphicalAdapter(turtle_lib)
        adapter.pen_down()

    def do_X(self, arg):
        """Go Along : X 100"""
        self.results.writeToFile("Go Along : X ", arg)
        self.parse(arg)
        turtle_lib = TurtleDrawerLib()
        adapter = GraphicalAdapter(turtle_lib)
        adapter.go_along(self.data)

    def do_Y(self, arg):
        """Go Down : Y 100"""
        self.results.writeToFile("Go Along : Y", arg)
        self.parse(arg)
        turtle_lib = TurtleDrawerLib()
        adapter = GraphicalAdapter(turtle_lib)
        adapter.go_down(self.data)

    def do_N(self, arg):
        """Draw line 0 degrees : N 100"""
        self.results.writeToFile("Draw line 0 degrees : N", arg)
        self.parse(arg)
        turtle_drawer = TurtleDrawer()
        turtle_drawer.draw_line(0, self.data)

    def do_E(self, arg):
        """Draw line 90 degrees : E 100"""
        self.results.writeToFile("Draw line 90 degrees : E", arg)
        self.parse(arg)
        turtle_drawer = TurtleDrawer()
        turtle_drawer.draw_line(90, self.data)

    def do_S(self, arg):
        """Draw line 120 degrees : S 100"""
        self.results.writeToFile("Draw line 120 degrees : S", arg)
        self.parse(arg)
        turtle_drawer = TurtleDrawer()
        turtle_drawer.draw_line(180, self.data)

    def do_W(self, arg):
        """Draw line 270 degrees : W 100"""
        self.results.writeToFile("Draw line 270 degrees : W", arg)
        self.parse(arg)
        turtle_drawer = TurtleDrawer()
        turtle_drawer.draw_line(270, self.data)

    def do_square(self, arg):
        """Draw Square: square 100"""
        self.results.writeToFile("Drawing a square")
        self.parse(arg)
        turtle_drawer = TurtleDrawer()
        directions = [0, 90, 180, 270]
        for i in directions:
            turtle_drawer.draw_line(i, self.data)

    def do_circle(self, arg):
        """Draw Circle: circle 50"""
        self.results.writeToFile("Drawing a circle")
        self.parse(arg)
        turtle_lib = TurtleDrawerLib()
        adapter = GraphicalAdapter(turtle_lib)
        adapter.pen_down()
        adapter.draw_circle(self.data)

    def do_triangle(self, arg):
        """Draw Circle: circle 50"""
        self.results.writeToFile("Drawing a triangle")
        self.parse(arg)
        turtle_lib = TurtleDrawerLib()
        adapter = GraphicalAdapter(turtle_lib)
        adapter.pen_down()
        adapter.draw_triangle(self.data)

    def do_Exit(self, arg):
        """Exit Turtle CMD"""
        self.results.writeToFile("End program, Bye")
        print("Bye")
        return True
