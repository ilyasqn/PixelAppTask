import re
from one import Base


class B(Base):
    def __init__(self):
        super().__init__()
        self._a = 'Result False'

    def func(self, string: str):
        """ регулярное выражение проверяет строки на соответствие
        определенному формату: три цифры, тире, от 3 до 5 строчных букв,
        тире и три заглавные буквы. Начальные и конечные пробелы игнорируются. от 3 до 5 потому что,
        "assert b.func('123-abcefe-ABC') is None" не удовлетворял бы условия {0, 3} и {0, 5}"""
        pattern = r"^\s*(\d{3}-[a-z]{3,5}-[A-Z]{3})\s*$"
        return re.match(pattern, string)
