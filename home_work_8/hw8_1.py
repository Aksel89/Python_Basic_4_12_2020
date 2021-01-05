"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    """Данная функция принимает дату в формате 'день-месяц-год'."""

    def __init__(self, day_month_year: str):
       self.day_month_year = day_month_year

    @classmethod
    def extraction(cls, day_month_year):
        int_data = []
        for itm in day_month_year.split():
            if itm != '-':
                assert isinstance(itm, str)
                int_data.append(itm)
        return f"Дата: {int(int_data[0])}.{int(int_data[1])}.{int(int_data[2])}"

    @staticmethod
    def validation(day: int, month: int, year: int):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return ('Введена верная дата')
                else:
                    return 'Введен неверный год!'
            else:
                return 'Введен неверный месяц!'
        else:
            return 'Введен неверный день!'


print(Data.extraction('05 - 01 - 2020'))
print(Data.validation(12, 1, 2020))
