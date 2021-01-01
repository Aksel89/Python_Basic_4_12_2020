"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clotes(ABC):

    @property
    @abstractmethod
    def parametrs(self):
        pass

    @property
    @abstractmethod
    def consumption(self):
        pass


class Costume(Clotes):

    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

    @property
    def parametrs(self):
        return f"{self.name} для клиента ростом {self.height} см."

    @property
    def consumption(self):
        return f"Расход ткани на костюм составит {2 * self.height + 0.3 : .2f}."


class Coat(Clotes):

    def __init__(self, name: str, size: float):
        self.name = name
        self.size = size

    @property
    def parametrs(self):
        return f"{self.name} {self.size} размера."

    @property
    def consumption(self):
        return f"Расход ткани на пальто составит {self.size / 6.5 + 0.3 : .2f}."


class TotalConsumption(Costume, Coat):

    def tot_cons(self):
        return f"Общий расход ткани составит: {self.size / 6.5 + 0.3 + 2 * self.height + 0.3 : .2f}"


coat1 = Coat('Пальто', 56)
print(coat1.parametrs, coat1.consumption)

costume1 = Costume('Костюм', 185)
print(costume1.parametrs, costume1.consumption)

total = TotalConsumption
print(total.tot_cons)
