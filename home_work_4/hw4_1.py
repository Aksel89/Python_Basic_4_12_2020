"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
from my_funcs import func_salary

salary = argv

while True:
    working_hours = input("Введите количество отработанных часов>>>\n")
    if working_hours.isdigit():
        working_hours = int(working_hours)
        break
    else:
        print("Это не число. Повторите ввод>>>\n")

while True:
    rate_per_hour = input("Введите ставку в час>>>\n")
    if rate_per_hour.isdigit():
        rate_per_hour = int(rate_per_hour)
        break
    else:
        print("Это не число. Повторите ввод>>>\n")

while True:
    bonus = input("Введите премию в процентах>>>\n")
    if bonus.isdigit():
        bonus = int(bonus)
        break
    else:
        print("Это не число. Повторите ввод>>>\n")

print("Имя скрипта: ", salary)
print("Всего отработано часов в месяц: ", working_hours)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)
print(func_salary(working_hours, rate_per_hour, bonus))

# Запустить из терминала файл hw4_1.py - скрипт запросит данные и выполнит подсчет З/П.
