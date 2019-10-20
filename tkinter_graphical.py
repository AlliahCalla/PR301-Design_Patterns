from abc import ABC, abstractmethod, abstractproperty
from typing import Any
from tkinter import *
from tkinter import ttk
from tkinter_drawer import TkinterDrawer
from writer import Writer


class WindowBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_button(self) -> None:
        pass

    @abstractmethod
    def produce_canvas(self) -> None:
        pass

    @abstractmethod
    def produce_scale(self) -> None:
        pass

    @abstractmethod
    def produce_label(self) -> None:
        pass

    @abstractmethod
    def produce_separator(self) -> None:
        pass


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self):
        print(self.parts)
        return self.parts

    def get_parts(self, no):
        print(id(self.parts))
        return self.parts[no]


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> WindowBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: WindowBuilder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self, text) -> None:
        self.builder.produce_button(text)

    def build_full_featured_product(self, text) -> None:
        self.builder.produce_button(text)
        self.builder.produce_canvas()
        self.builder.produce_scale()


class ConcreteBuilder1(WindowBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def produce_button(self, root, text: str) -> None:
        self._product.add(Button(root, text=text))

    def produce_canvas(self, root, background: str, w, h) -> None:
        self._product.add(Canvas(root, bg=background, width=w, height=h))

    def produce_scale(self,root, fr, t, ort) -> None:
        self._product.add(Scale(root, from_=fr, to=t, orient=ort))

    def produce_label(self, root, t) -> None:
        self._product.add(Label(root, text=t))

    def produce_separator(self, root, ort) -> None:
        self._product.add(ttk.Separator(root, orient=ort))


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    # print("Standard basic product: ")
    # director.build_minimal_viable_product("text")
    # builder.product.list_parts()

    # print("\n")

    # print("Standard full featured product: ")
    # director.build_full_featured_product("text")
    # builder.product.list_parts()

    # print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_canvas('white', 500, 500)
    builder.produce_label("Pen Size: ")
    builder.produce_scale(1, 2, HORIZONTAL)
    builder.produce_separator(VERTICAL)
    builder.produce_button(' → ')
    builder.produce_button(' ← ')
    builder.produce_button('  ↑  ')
    builder.produce_button('  ↓  ')
    builder.produce_button('Pen up')
    builder.produce_button('Pen down')
    builder.produce_button('Clear Canvas')
    builder.produce_button('square')
    builder.produce_button('circle')
    builder.produce_button('triangle')
    builder.product.list_parts()


class TkinterGraphical(TkinterDrawer, Product1):

    def __init__(self):
        self.root = Tk()
        self.temp = []
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
        director = Director()
        self.builder = ConcreteBuilder1()
        director.builder = self.builder

    def __create_button(self, text):
        self.builder.produce_button(self.root, text)

    def __create_label(self, t):
        self.builder.produce_label(self.root, t)

    def __create_scale(self, fr, t, ort):
        self.builder.produce_scale(self.root, fr, t, ort)

    def __create_canvas(self, background, w, h):
        self.builder.produce_canvas(self.root, background, w, h)

    def __create_separator(self, ort):
        self.builder.produce_separator(self.root,ort)

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
        # self.label.append(self.builder.product.get_parts(1))

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
        #building elements
        self.__setup_canvas()
        self.__setup_label()
        self.__setup_scale()
        self.__setup_button()
        self.__setup_separator()

        #Appending elements
        self.temp = self.builder.product.list_parts()
        self.canvas.append(self.temp[0])
        print("My Canvas:")
        print (self.canvas)
        self.label.append(self.temp[1])
        print("\nMy Label:" )
        print(self.label)
        self.scales.append(self.temp[2])
        print("\nMy Scale:")
        print(self.scales)
        self.buttons.append(self.temp[3])
        self.buttons.append(self.temp[4])
        self.buttons.append(self.temp[5])
        self.buttons.append(self.temp[6])
        self.buttons.append(self.temp[7])
        self.buttons.append(self.temp[8])
        self.buttons.append(self.temp[9])
        self.buttons.append(self.temp[10])
        self.buttons.append(self.temp[11])
        self.buttons.append(self.temp[12])
        print("\nMy Buttons:")
        print(self.buttons)
        self.separator.append(self.temp[13])
        print("\nMy Separator:")
        print(self.separator)


        #Position
        self.__setup_canvas_position()
        self.__setup_label_position()
        self.__setup_scale_position()
        self.line_width = self.scales[0].get()
        self.__setup_button_grid()
        self.__setup_button_position()
        self.__setup_button_y()
        self.__setup_button_methods()
        self.__setup_separator_position()
        self.__finalize()
        self.start()
        #self.builder.product.get_parts(0)
        #self.builder.product.get_parts(1)

        #clean the code up

