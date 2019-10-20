from tkinter_builder import TkinterBuilder
from tk_user_interface import TkUserInterface
from tkinter_drawer import TkinterDrawer
from tkinter import *


class TkinterGraphicalBuilder(TkinterBuilder, TkinterDrawer):

    def __init__(self):
        self.tkinter_user_interface = TkUserInterface()
        self.buttons = []
        self.root = Tk()
        self.canvas = []
        self.scales = []
        self.separator = []
        self.label = []
        self.line_width = self.tkinter_user_interface.get_line_weight()
        self.pen_state = self.tkinter_user_interface.get_pen_state()
        self.x = 250
        self.y = 250
        self.file = self.tkinter_user_interface.get_file()
        self.color = self.tkinter_user_interface.get_color()
        self.choose_size_button = self.tkinter_user_interface.get_choose_size_button()
        self.direction = self.tkinter_user_interface.get_direction()
        self.distance = self.tkinter_user_interface.get_distance()

    def build_buttons(self) -> None:
        self.tkinter_user_interface.set_button(self.root, ' → ')
        self.tkinter_user_interface.set_button(self.root, ' ← ')
        self.tkinter_user_interface.set_button(self.root, '  ↑  ')
        self.tkinter_user_interface.set_button(self.root, '  ↓  ')
        self.tkinter_user_interface.set_button(self.root, 'Pen up')
        self.tkinter_user_interface.set_button(self.root, 'Pen down')
        self.tkinter_user_interface.set_button(self.root, 'Clear Canvas')
        self.tkinter_user_interface.set_button(self.root, 'square')
        self.tkinter_user_interface.set_button(self.root, 'circle')
        self.tkinter_user_interface.set_button(self.root, 'triangle')
        self.buttons = self.tkinter_user_interface.get_button()
        self.__setup_button_methods()
        self.__setup_button_grid()
        self.__setup_button_position()
        self.__setup_button_y()
        self.__setup_button_methods()

    def build_label(self) -> None:
        self.tkinter_user_interface.set_label(self.root, "Pen Size: ")
        self.label = self.tkinter_user_interface.get_label()
        self.__setup_label_position()

    def build_canvas(self) -> None:
        self.tkinter_user_interface.set_canvas(self.root, 'white', 500, 500)
        self.canvas = self.tkinter_user_interface.get_canvas()
        self.__setup_canvas_position()

    def build_scales(self) -> None:
        self.tkinter_user_interface.set_scales(self.root, 1, 2, HORIZONTAL)
        self.scales = self.tkinter_user_interface.get_scales()
        self.__setup_scale_position()

    def build_separator(self) -> None:
        self.tkinter_user_interface.set_separator(self.root, VERTICAL)
        self.separator = self.tkinter_user_interface.get_separator()
        self.__setup_separator_position()

    def build_binder(self) -> None:
        self.file.writeToFile("Pen size", self.choose_size_button)
        self.file.writeToFile("X position", self.x)
        self.file.writeToFile("Y position", self.y)
        self.file.writeToFile("Pen color", self.color)
        self.line_width = self.scales[0].get()
        self.canvas[0].grid(row=60, columnspan=60)
        self.tkinter_user_interface.set_line_weight(self.scales[0].get())
        self.canvas[0].bind('<B1-Motion>', self.draw_line)
        self.canvas[0].bind('<ButtonRelease-1>', self.reset)
        self.start()
        self.root.mainloop()

    def get_user_interface(self) -> TkUserInterface():
        return self.tkinter_user_interface

    def __assign_position(self, element, r, c, s, px, py):
        element.grid(row=r, column=c, sticky=s, padx=px, pady=py)

    def __assign_row_grid(self, element, rowNum, w):
        element.grid_rowconfigure(rowNum, weight=w)

    def __assign_col_grid(self, element, colNum, w):
        element.grid_rowconfigure(colNum, weight=w)

    def __assign_grid(self, element, r, c):
        element.grid(row=r, column=c)

    def __assign_padding_x(self, element, x):
        element.grid(padx=x)

    def __assign_padding_y(self, element, y):
        element.grid(pady=y)

    def __setup_button_methods(self):
        self.buttons[0].config(command=lambda: self.draw_line(0, 50))
        self.buttons[1].config(command=lambda: self.draw_line(180, 50))
        self.buttons[2].config(command=lambda: self.draw_line(90, 50))
        self.buttons[3].config(command=lambda: self.draw_line(270, 50))
        self.buttons[4].config(command=lambda: self.pen_up())
        self.buttons[5].config(command=lambda: self.pen_down())
        self.buttons[6].config(command=lambda: self.reset())
        self.buttons[7].config(command=lambda: self.draw_square())
        self.buttons[8].config(command=lambda: self.draw_circle())
        self.buttons[9].config(command=lambda: self.draw_triangle())

    def __setup_canvas_position(self):
        self.__assign_row_grid(self.canvas[0], 0, 1)
        self.__assign_col_grid(self.canvas[0], 0, 1)

    def __setup_label_position(self):
        self.__assign_grid(self.label[0], 1, 4)
        self.__assign_padding_y(self.label[0], 12)

    def __setup_scale_position(self):
        self.__assign_grid(self.scales[0], 1, 5)

    def __setup_separator_position(self):
        self.__assign_position(self.separator[0], 1, 3, NS, 0, 0)

    def __setup_button_position(self):
        self.__assign_position(self.buttons[0], 1, 2, W, 10, 0)
        self.__assign_position(self.buttons[1], 1, 0, E, 10, 0)
        self.__assign_position(self.buttons[2], 0, 1, SW, 0, 0)
        self.__assign_position(self.buttons[3], 2, 1, NW, 0, 0)

    def __setup_button_grid(self):
        self.__assign_grid(self.buttons[4], 0, 4)
        self.__assign_grid(self.buttons[5], 0, 5)
        self.__assign_grid(self.buttons[6], 0, 6)
        self.__assign_grid(self.buttons[7], 2, 4)
        self.__assign_grid(self.buttons[8], 2, 5)
        self.__assign_grid(self.buttons[9], 2, 6)

    def __setup_button_y(self):
        self.__assign_padding_y(self.buttons[4], 10)
        self.__assign_padding_y(self.buttons[5], 10)
        self.__assign_padding_y(self.buttons[6], 10)
        self.__assign_padding_y(self.buttons[7], 10)
        self.__assign_padding_y(self.buttons[9], 10)
