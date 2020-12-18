"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(one, two, three):
    """
    Возвращает сумму двух наибольшших аргументов.
    :param one:
    :param two:
    :param three:
    :return:
    """
    return max(one + two, two + three, three + one)
print(my_func(3, 5, 7))