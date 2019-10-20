from abc import ABC, abstractmethod, abstractproperty
from typing import Any
from tkinter import *
from tkinter import ttk
from tkinter_graphical import *


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
        print (self.parts)

    def get_part(self, no):
        print( self.parts[no])


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

    def build_full_featured_product(self,text) -> None:
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
        self.root = Tk()

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

    def produce_button(self, text:str) -> None:
        self._product.add(Button(self.root, text=text))

    def produce_canvas(self, background:str, w, h) -> None:
        self._product.add(Canvas(self.root, bg=background, width=w, height=h))

    def produce_scale(self, fr, t, ort) -> None:
        self._product.add(Scale(self.root, from_=fr, to=t, orient=ort))

    def produce_label(self,t) -> None:
        self._product.add(Label(self.root, text=t))

    def produce_separator(self,ort) -> None:
        self._product.add(ttk.Separator(self.root, orient=ort))

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    #print("Standard basic product: ")
    #director.build_minimal_viable_product("text")
    #builder.product.list_parts()


    #print("\n")

    #print("Standard full featured product: ")
    #director.build_full_featured_product("text")
    #builder.product.list_parts()

    #print("\n")

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
    #print(builder.product.get_part(0))
