"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name: str, speed: int, color: str, is_police: bool = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"Автомобиль {self.name} начал движение."

    def stop(self):
        return f"Автомобиль {self.name} закончил движение."

    def turn(self, direction):
        if direction in "прямо":
            return f"Автомобиль {self.name} движется {direction}."
        elif direction in "назад":
            return f"Автомобиль {self.name} развернулся."
        elif direction in ("лево", "право"):
            return f"Автомобиль {self.name} повернул на{direction}."
        else:
            raise ValueError("Напрвление движения может быть только прямо, налево, направо и назад!")

    def show_speed(self):
        return f"Скорость автомобиля {self.name} - {self.speed} км/ч."


class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)

    def show_speed(self):
        if self.speed > 60:
            return f"Внимание!!! Вы превысили скорость на {self.speed - 60} км/ч!"
        else:
            return "Скорость в норме."


class WorkCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)

    def show_speed(self):
        if self.speed > 40:
            return f"Внимание!!! Вы превысили скорость на {self.speed - 40} км/ч!"
        else:
            return "Скорость в норме."


class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, False)


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


town = TownCar("KIA", 70, "черный")
print(town.go(), town.show_speed(), town.turn("лево"), town.stop())

work = WorkCar("Камаз", 40, "зеленый")
print(work.go(), work.show_speed(), work.turn("назад"), work.turn("прямо"), work.stop())

sport = SportCar("Lamborgini", 200, "желтый")
print(sport.go(), sport.color, sport.show_speed(), sport.turn("прямо"), sport.stop(), sport.is_police)

police = PoliceCar("УАЗ", 80, "бело-синий")
print(police.go(), police.show_speed(), police.turn("прямо"), police.stop(), police.is_police)
