"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки с помощью {self.title}"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки с помощью {self.title}"

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки с помощью {self.title}"

draw_pen = Pen("гелевая ручка")
print(draw_pen.draw())

draw_pencil = Pencil("восковой карандаш")
print(draw_pencil.draw())

draw_handle = Handle("красный маркер")
print(draw_handle.draw())