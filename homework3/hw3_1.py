"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_fun(divisible, divider) -> float:
    """
    Функция возвращает частное от деления 1-го числа на 2-е.
    :param divisible: float: делимое
    :param divider: float: делитель
    :return: float: частное
    """
    try:
        divisible = float(input("Введите делимое>>> "))
        divider = float(input("Введите делитель>>> "))
    except ValueError:
        print("Вы ввели не число!")
        return
    try:
        result = divisible / divider
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        return
    return result

print(my_fun("", ""))
