"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class OfficeEquipmentWarehouse:
    storage: dict = {}

    def add_equipment(self, equipment, count):
        equipment_type = equipment.__class__.__name__
        try:
            self.storage[equipment_type][equipment.name] += count
        except KeyError:
            if equipment_type not in self.storage:
                self.storage[equipment_type] = {}
                self.storage[equipment_type][equipment.name] = count
            elif equipment.name not in self.storage[equipment_type]:
                self.storage[equipment_type][equipment.name] = count

    def __str__(self):
        output = ''
        for itm, equipment in self.storage.items():
            output += f'{itm}:\n'
            print(equipment)
            for i, count in equipment.items():
                output += f'\t{i} {count}\n'

        return output


class OfficeEquipment:

    def __init__(self, name: str, weight: float, price: float):
        self.name = name
        self.weight = weight
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        try:
            self.__price = float(price)
        except ValueError:
            print(f"Цена должна быть натуральным числом!")

    def __str__(self):
        return f'{self.name}, цена: {self.price}руб, вес: {self.weight}кг.'


class Printer(OfficeEquipment):
    print_format = ["A2", "A3", "A4", "A5"]
    print_color = ["цветной", "черно-белый"]

    def __init__(self, name: str, weight: float, price: float, print_format: str, print_color: str):
        super(Printer, self).__init__(name, weight, price)
        self.print_format = print_format
        self.print_color = print_color

    def __str__(self):
        return f'{self.print_color} принтер:{self.name}, формата {self.print_format}. Стоимость: {self.price}руб, вес: {self.weight}кг'


class Scaner(OfficeEquipment):
    scan_format = ["A2", "A3", "A4", "A5"]

    def __init__(self, name: str, weight: float, price: float, scan_format: str):
        super(Scaner, self).__init__(name, weight, price)
        self.scan_format = scan_format

    def __str__(self):
        return f'Сканер {self.name}, формат: {self.scan_format}. Стоимость: {self.price}руб, вес: {self.weight}кг'


class Xerox(OfficeEquipment):
    copy_format = ["A4", "A5", "A6"]

    def __init__(self, name: str, weight: float, price: float, copy_format: str):
        super(Xerox, self).__init__(name, weight, price)
        self.copy_format = copy_format

    def __str__(self):
        return f'Сканер {self.name}, формат: {self.copy_format}. Стоимость: {self.price}руб, вес: {self.weight}кг'
