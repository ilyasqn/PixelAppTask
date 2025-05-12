from abc import ABC, abstractmethod


class Error(Exception):
    def __str__(self):
        return "error one"


class UndefinedError(Exception):
    def __str__(self):
        return "None prohibited"

    def message(self, arg=None):
        if arg == 1:
            return "error message one"
        elif arg == 2:
            return "error message two"
        return "error message"


class Base(ABC):
    def __init__(self):
        self._a = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value is None:
            raise UndefinedError()
        if isinstance(value, str):
            raise Error()
        self._a = value

    def value(self):
        return self._a

    @abstractmethod
    def func(self, *args, **kwargs):
        pass


class A(Base):
    def __init__(self):
        super().__init__()
        self._a = 'Result True'

    def func(self, val=None):
        if val is None:
            if not isinstance(self._a, int):
                raise AttributeError("Invalid type for _a")
            return self._a * 3 * 5
        return val * val * 3
