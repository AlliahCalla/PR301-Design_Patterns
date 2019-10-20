from abc import ABCMeta, abstractmethod
from tk_user_interface import TkUserInterface


class TkinterBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_buttons(self) -> None:
        pass

    @abstractmethod
    def build_label(self) -> None:
        pass

    @abstractmethod
    def build_canvas(self) -> None:
        pass

    @abstractmethod
    def build_scales(self) -> None:
        pass

    @abstractmethod
    def build_separator(self) -> None:
        pass

    @abstractmethod
    def build_binder(self) -> None:
        pass

    @abstractmethod
    def get_user_interface(self) -> TkUserInterface():
        pass
