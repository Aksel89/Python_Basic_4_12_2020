"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def my_function(name = None,
                surname = None,
                year_of_birth = None,
                city = None,
                e_mail = None,
                phone = None):
    """
    Функция обрабатывает значения аргументов и
    выводит информацию о пользователе в одну строку.
    :param name: str
    :param surname: str
    :param year_of_birth: int
    :param city: str
    :param e_mail: str
    :param phone: int
    :return: str
    """
    return f"Пользователь {name} {surname}, {year_of_birth} года рождения. Проживает в {city}. Контактные данные: e-mail:{e_mail}, телефон:{phone}."

print(my_function(name="Николай", year_of_birth= 1983, phone= 25673459856, surname="Иванов", city="Омск", e_mail= "gdgdf@mail.com" ))
