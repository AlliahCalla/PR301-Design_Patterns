from tigr import AbstractDrawer
from tkinter import *
from tkinter import ttk
from writer import *
import math


# Alliah & Chris

class TkinterDrawer(AbstractDrawer):

    def select_pen(self, pen_num):
        self.line_width = self.choose_size_button.get()
        self.file.writeToFile("Pen size", self.line_width)

    def pen_down(self):
        self.pen_state = True
        self.file.writeToFile("Is pen down ?", self.pen_state)

    def pen_up(self):
        self.pen_state = False
        self.file.writeToFile("Is pen down ?", self.pen_state)

    def go_along(self, along):
        self.x = along
        self.file.writeToFile("New X Position", self.x)

    def go_down(self, down):
        self.y = down
        self.file.writeToFile("New Y Position", self.y)

    def draw_line(self, direction, distance):
        if not self.pen_state:
            self.color = "white"
        else:
            self.color = "black"
        self.file.writeToFile("Pen color", self.color)

        if direction == 0:
            new_direction = 0

        if direction == 180:
            new_direction = 180
        if direction == 90:
            new_direction = 270
        if direction == 270:
            new_direction = 90

        angle_in_radians = new_direction * math.pi / 180

        line_length = distance
        center_x = self.x
        center_y = self.y

        end_x = center_x + line_length * math.cos(angle_in_radians)
        end_y = center_y + line_length * math.sin(angle_in_radians)
        self.line_width = self.scales[0].get()
        self.canvas[0].create_line(self.x, self.y, end_x, end_y,
                                   fill=self.color, width=self.line_width)
        self.x = end_x
        self.y = end_y
        self.file.writeToFile("New X position", self.x)
        self.file.writeToFile("New Y position", self.y)

    def draw_square(self):
        self.file.writeToFile("We are drawing a square")
        if self.pen_state:
            directions = [0, 90, 180, 270]
            for i in directions:
                self.draw_line(i, 50)

    def draw_circle(self):
        self.file.writeToFile("We are drawing a circle")
        r = 50
        if self.pen_state:
            self.canvas[0].create_oval(self.x - r, self.y - r,
                                       self.x + r, self.y + r,
                                       width=self.line_width)

    def draw_triangle(self):
        if self.pen_state:
            self.file.writeToFile("We are drawing a triangle")
            self.canvas[0].create_line(55, 85, 155, 85, 105,
                                   180, 55, 85, width=self.line_width)

    def reset(self):
        self.file.writeToFile("We are restting")
        self.x = 250
        self.y = 250
        self.canvas[0].delete("all")
        self.file.writeToFile("Back to original X coordinate", self.x)
        self.file.writeToFile("Back to original Y coordinate", self.y)

    def start(self):
        self.file.writeToFile("Starting TKinter Drawer. Here we go ! ")
