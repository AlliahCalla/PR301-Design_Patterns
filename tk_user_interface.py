from typing import Any
from tkinter import *
from writer import Writer
from tkinter_drawer import ttk

from tk_user_interface_plan import TkinterInterfacePlan


class TkUserInterface(TkinterInterfacePlan):

    def __init__(self):
        self.buttons = []
        self.canvas = []
        self.scales = []
        self.separator = []
        self.label = []
        self.x = 0
        self.y = 0
        self.file = Writer("TKInterDrawer_Result.txt")
        self.pen_state = True
        self.color = "black"
        self.choose_size_button = 1
        self.line_weight = 1
        self.direction = 0
        self.distance = 0

    def set_button(self, root, text: str) -> None:
        self.buttons.append(Button(root, text=text))

    def set_label(self, root, t: str) -> None:
        self.label.append(Label(root, text=t))

    def set_canvas(self, root, background: object, w: object,
                   h: object) -> None:
        self.canvas.append(Canvas(root, bg=background, width=w, height=h))

    def set_scales(self, root, fr: object, t: object, ort: object) -> None:
        self.scales.append((Scale(root, from_=fr, to=t, orient=ort)))

    def set_separator(self, root, ort: object) -> None:
        self.separator.append(ttk.Separator(root, orient=ort))

    def set_x(self, x: int) -> None:
        self.x = x

    def set_y(self, y: int) -> None:
        self.y = y

    def set_file(self, file: Any) -> None:
        self.file = file

    def set_pen_state(self, state: bool) -> None:
        self.pen_state = state

    def set_color(self, color: str) -> None:
        self.color = color

    def set_choose_size_button(self, size: int) -> None:
        self.choose_size_button = size

    def set_line_weight(self, weight: int) -> None:
        self.line_weight = weight

    def set_direction(self, direction: int) -> None:
        self.direction = direction

    def set_distance(self, distance: int) -> None:
        self.distance = distance

    def get_button(self) -> object:
        return self.buttons

    def get_label(self):
        return self.label

    def get_canvas(self) -> object:
        return self.canvas

    def get_scales(self) -> object:
        return self.scales

    def get_separator(self) -> object:
        return self.separator

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_file(self) -> Any:
        return self.file

    def get_pen_state(self) -> bool:
        return self.pen_state

    def get_color(self) -> str:
        return self.color

    def get_choose_size_button(self) -> int:
        return self.choose_size_button

    def get_line_weight(self) -> int:
        return self.line_weight

    def get_direction(self) -> int:
        return self.direction

    def get_distance(self) -> int:
        return self.distance
