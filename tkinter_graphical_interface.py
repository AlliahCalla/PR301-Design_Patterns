from tkinter import *
from tkinter_drawer import ttk
from tkinter_drawer import TkinterDrawer
from writer import Writer


class TkinterGraphicInterface(TkinterDrawer):

    def __init__(self):
        self.root = Tk()
        self.buttons = []
        self.canvas = []
        self.entry = []
        self.scales = []
        self.separator = []
        self.label = []
        self.x = 0
        self.y = 0
        self.file = Writer("TKInterDrawer_Result.txt")
        self.pen_state = True
        self.color = "black"
        self.choose_size_button = 1
        self.line_width = 1
        self.direction = 0
        self.distance = 0

    def __create_button(self, text):
        self.buttons.append(Button(self.root, text=text))

    def __create_label(self, t):
        self.label.append(Label(self.root, text=t))

    def __create_scale(self, fr, t, ort):
        self.scales.append((Scale(self.root, from_=fr, to=t, orient=ort)))

    def __create_canvas(self, background, w, h):
        self.canvas.append(Canvas(self.root, bg=background, width=w, height=h))

    def __create_separator(self, ort):
        self.separator.append(ttk.Separator(self.root, orient=ort))

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

    def __setup_canvas(self):
        self.__create_canvas('white', 500, 500)

    def __setup_canvas_position(self):
        self.__assign_row_grid(self.canvas[0], 0, 1)
        self.__assign_col_grid(self.canvas[0], 0, 1)

    def __setup_label(self):
        self.__create_label("Pen Size: ")

    def __setup_label_position(self):
        self.__assign_grid(self.label[0], 1, 4)
        self.__assign_padding_y(self.label[0], 12)

    def __setup_scale(self):
        self.__create_scale(1, 2, HORIZONTAL)

    def __setup_scale_position(self):
        self.__assign_grid(self.scales[0], 1, 5)

    def __setup_separator(self):
        self.__create_separator(VERTICAL)

    def __setup_separator_position(self):
        self.__assign_position(self.separator[0], 1, 3, NS, 0, 0)

    def __setup_button(self):
        self.__create_button(' → ')
        self.__create_button(' ← ')
        self.__create_button('  ↑  ')
        self.__create_button('  ↓  ')
        self.__create_button('Pen up')
        self.__create_button('Pen down')
        self.__create_button('Clear Canvas')
        self.__create_button('square')
        self.__create_button('circle')
        self.__create_button('triangle')

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

    def __finalize(self):
        self.canvas[0].grid(row=60, columnspan=60)
        self.line_width = self.scales[0].get()
        self.canvas[0].bind('<B1-Motion>', self.draw_line)
        self.canvas[0].bind('<ButtonRelease-1>', self.reset)

    def setup(self):
        self.root.geometry("510x645")
        self.choose_size_button = 1
        self.x = 250
        self.y = 250

        # Idea of getting value to be stored in txt file for testing
        self.file.writeToFile("Pen size", self.choose_size_button)
        self.file.writeToFile("X position", self.x)
        self.file.writeToFile("Y position", self.y)
        self.file.writeToFile("Pen color", self.color)

        self.__setup_canvas()
        self.__setup_canvas_position()
        self.__setup_label()
        self.__setup_label_position()
        self.__setup_scale()
        self.__setup_scale_position()
        self.line_width = self.scales[0].get()
        self.__setup_button()
        self.__setup_button_grid()
        self.__setup_button_position()
        self.__setup_button_y()
        self.__setup_button_methods()
        self.__setup_separator()
        self.__setup_separator_position()
        self.__finalize()
        self.start()
