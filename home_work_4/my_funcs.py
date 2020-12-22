def func_salary(working_hours: "int", rate_per_hour: "int", bonus: "int") -> str:
    """
    Функция считает зарплату работника в зависимости от введеных данных: количество отработанных часов *
    ставка за час работы - это основная оплата труда и + премия % от основной оплаты труда (0 если премии нет)
    :return:
    :param working_hours: int: количество отработанных часов
    :param rate_per_hour: int: ставка за час работы
    :param bonus: int: премия в % (целое число без знака %)
    :return: str:
    """
    net_salary = working_hours * rate_per_hour
    if bonus > 0:
        salary_from_bonus = net_salary + (net_salary * bonus / 100)
        return f"Зарплата в этом месяце, с учетом премии, составила: {salary_from_bonus}"
    else:
        return f"Увы, в этом месяце без премии. Зарплата составила: {net_salary}"


def fact(num):
    """
    Функция расчитывает факториал введеного числа.

    :param num: int: введеное число
    :return:
    """
    count = 1
    for itm in range(1, num + 1):
        count *= itm
        yield count
    print(f"Факториал {num} равен {count}")
