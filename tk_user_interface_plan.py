from typing import Any
from abc import ABCMeta, abstractmethod


class TkinterInterfacePlan(metaclass=ABCMeta):

    @abstractmethod
    def set_button(self, root, text: str) -> None:
        pass

    @abstractmethod
    def set_canvas(self, root, background: str, w: int, h: int) -> None:
        pass

    @abstractmethod
    def set_label(self, root, t: str) -> None:
        pass

    @abstractmethod
    def set_scales(self, root, fr: int, t: int, ort: Any) -> None:
        pass

    @abstractmethod
    def set_separator(self, root, ort: Any) -> None:
        pass
