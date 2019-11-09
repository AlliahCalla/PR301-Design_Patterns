from tkinter_builder import TkinterBuilder


class TkinterDirector(object):
    def __init__(self, tkinter_builder: TkinterBuilder):
        self.tkinter_builder = tkinter_builder

    def get_user_interface(self):
        return self.tkinter_builder

    def construct_user_interface(self):
        self.tkinter_builder.build_canvas()
        self.tkinter_builder.build_buttons()
        self.tkinter_builder.build_label()
        self.tkinter_builder.build_scales()
        self.tkinter_builder.build_separator()
        self.tkinter_builder.build_binder()
