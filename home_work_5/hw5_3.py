"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import os

my_file = os.path.join(os.path.dirname(__file__), "file_5_3.txt")

employee_dict = {}
with open(my_file, 'r', encoding="UTF-8") as file:
    for line in file:
        key, value = line.split()
        employee_dict[key] = value


family = []
money = []
min_salary = 20000
for key, value in employee_dict.items():
    money.append(int(value))
    average_salary = sum(money) / len(money)
    if int(value) < min_salary:
        family.append(key)
        print(f"Сотрудник: {key} имеют зарплату ниже {min_salary}")
print(f"Средний оклад по сотрудникам составляет {average_salary}")



