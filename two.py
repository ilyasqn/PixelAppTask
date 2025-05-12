import re
from one import Base


class B(Base):
    def __init__(self):
        super().__init__()
        self._a = 'Result False'

    def func(self, string: str):
        pattern = r"^\s*(\d{3}-[a-z]{3,5}-[A-Z]{3})\s*$"
        return re.match(pattern, string)
