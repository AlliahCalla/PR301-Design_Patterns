from tigr import AbstractDrawer
import turtle


class TurtleDrawerLib(AbstractDrawer):
    def __init__(self):
        self.pen_list = ["", "white", "black", "red", "yellow", "blue"]
        self.turtle = turtle
        self.pen_up()
        self.triangle_size = 1

    def select_pen(self, pen_num):
        if int(pen_num) > 5 or int(pen_num) < 1:
            print("Only use pens 1-5")
        else:
            self.turtle.pencolor(self.pen_list[int(pen_num)])

    def pen_down(self):
        self.turtle.pendown()

    def pen_up(self):
        self.turtle.penup()

    def go_along(self, along):
        current_x = self.turtle.xcor()
        if self.turtle.isdown():
            self.turtle.penup()
            self.turtle.setx(current_x + int(along))
            self.turtle.pendown()
        else:
            self.turtle.setx(current_x + int(along))

    def go_down(self, down):
        current_y = self.turtle.ycor()
        if self.turtle.isdown():
            self.turtle.penup()
            self.turtle.sety(current_y + int(down))
            self.turtle.pendown()
        else:
            self.turtle.sety(current_y + int(down))

    def draw_line(self, direction, distance):
        direction = int(direction)
        distance = int(distance)
        if direction == 90 or direction == 270:
            direction -= 90
        else:
            direction += 90
        self.turtle.seth(direction)
        if self.turtle.isdown():
            self.turtle.forward(distance)

    def draw_circle(self, size):
        size = int(size)
        self.turtle.circle(size)

    def draw_rectangle(self, size):
        our_direction = 0
        for i in range(4):
            self.draw_line(our_direction, size)
            our_direction += 90

    def draw_triangle(self, size):
        size = int(size)
        self.turtle.seth(0)
        for i in range(3):
            self.turtle.left(120)
            self.turtle.forward(1 * size * self.triangle_size)

    def get_state(self):
        return self.triangle_size

    def set_state(self, new_state):
        self.triangle_size = new_state
        print("\nTurtleDrawer has CHANGED")
        self.notify()
