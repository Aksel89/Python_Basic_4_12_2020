"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import os

my_file = os.path.join(os.path.dirname(__file__), "file_5_6.txt")
my_dict = {}

with open(my_file, 'r', encoding="UTF-8") as file:
    for line in file:
        date = line.split(':')
        my_dict[date[0]] = date[1].split()
    print(my_dict)

hours_lesson = {}
for key, value in my_dict.items():
    hours_lesson[key] = 0
    for itm in value:
        try:
            hours_lesson[key] += float(itm.split('(')[0])
        except ValueError:
            continue
print(hours_lesson)



