"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


class Division:
    def __init__(self, divisible: float, divider: float) -> float:
        self.divisible = divisible
        self.divider = divider

    def div(self):

        if self.divider != 0:
            return f"{self.divisible / self.divider: .2f}"
        else:
            return DivisionByZero("Делить на ноль - нельзя!")



result = Division(10, 0)
print(result.div())
