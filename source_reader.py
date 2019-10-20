from tigr import AbstractSourceReader
from parsers import ArgumentParser
from tkinter_graphical_interface import TkinterGraphicInterface
from turtle_prompt import TurtlePrompt
from writer import Writer
#from tkinter_graphical import *
from tkinter_director import TkinterDirector
from tkinter_graphical_builder import TkinterGraphicalBuilder
from tkinter_drawer import TkinterDrawer
from turtle_drawer import TurtleDrawer


class ArgumentSourceReader(AbstractSourceReader):

    results = Writer("SourceReader_Result.txt")



    def go(self):
        result = ArgumentParser.parse(self, '')
        if result == 'g':
            print('graphics')
            self.results.writeToFile("Graphics")
        elif result == 't':

            self.results.writeToFile("Running Turtle Command")
            TurtlePrompt().cmdloop()
        elif result == 'k':
            tkinter_drawer = TkinterDrawer
            self.results.writeToFile("Running TKInter Drawer")
            tkinter_product = TkinterGraphicalBuilder(tkinter_drawer)
            tkinter_int = TkinterDirector(tkinter_product)
            tkinter_int.construct_user_interface()
        elif result == 'e':
            self.results.writeToFile("Exiting program")
            exit()
        else:
            self.results.writeToFile("Graphics from else "
                                     "+as arguments were wrong")
            print('graphics')


if __name__ == '__main__':
    s = ArgumentSourceReader(ArgumentParser(''))
    s.go()
