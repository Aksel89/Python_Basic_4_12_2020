"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": 0, "bonus": 0}

class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position)
        self._income['salary'] = salary
        self._income['bonus'] = bonus


    def get_full_name(self):
        return f"Сотрудник: {self.name} {self.surname}."

    def get_total_income(self):
        return f"Зарплата с учетом премии {sum(self._income.values())} дублонов."


worker1 = Position("Виктор", "Фомин", "Директор", 20000, 8000)
print(worker1.get_full_name(), worker1.get_total_income())
print(worker1.get_full_name(), worker1.position)
