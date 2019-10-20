from turtle_drawer import TurtleDrawer
from cmd import Cmd
from writer import *
from tigr import AbstractParser


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
        TurtleDrawer.select_pen(self, self.data)

    def do_U(self, arg):
        """Pen Up : U"""
        self.results.writeToFile("Pen is up", arg)
        self.parse(arg)
        TurtleDrawer.pen_up(self.command)

    def do_D(self, arg):
        """Pen Down : D"""
        self.results.writeToFile("Pen is down", arg)
        self.parse(arg)
        TurtleDrawer.pen_down(self.command)

    def do_X(self, arg):
        """Go Along : X 100"""
        self.results.writeToFile("Go Along : X ", arg)
        self.parse(arg)
        TurtleDrawer.go_along(self, self.data)

    def do_Y(self, arg):
        """Go Down : Y 100"""
        self.results.writeToFile("Go Along : Y", arg)
        self.parse(arg)
        TurtleDrawer.go_down(self, self.data)

    def do_N(self, arg):
        """Draw line 0 degrees : N 100"""
        self.results.writeToFile("Draw line 0 degrees : N", arg)
        self.parse(arg)
        TurtleDrawer.draw_line(self, 0, self.data)

    def do_E(self, arg):
        """Draw line 90 degrees : E 100"""
        self.results.writeToFile("Draw line 90 degrees : E", arg)
        self.parse(arg)
        TurtleDrawer.draw_line(self, 90, self.data)

    def do_S(self, arg):
        """Draw line 120 degrees : S 100"""
        self.results.writeToFile("Draw line 120 degrees : S", arg)
        self.parse(arg)
        TurtleDrawer.draw_line(self, 180, self.data)

    def do_W(self, arg):
        """Draw line 270 degrees : W 100"""
        self.results.writeToFile("Draw line 270 degrees : W", arg)
        self.parse(arg)
        TurtleDrawer.draw_line(self, 270, self.data)

    def do_square(self, arg):
        """Draw Square: square 100"""
        self.results.writeToFile("Drawing a square")
        self.parse(arg)
        directions = [0, 90, 180, 270]
        for i in directions:
            TurtleDrawer.draw_line(self, i, self.data)

    def do_circle(self, arg):
        """Draw Circle: circle 50"""
        self.results.writeToFile("Drawing a circle")
        self.parse(arg)
        TurtleDrawer.draw_circle(self, self.data)

    def do_Exit(self, arg):
        """Exit Turtle CMD"""
        self.results.writeToFile("End program, Bye")
        print("Bye")
        return True
