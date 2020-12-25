"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
import os

my_file_read = os.path.join(os.path.dirname(__file__), "file_5_4_1.txt")
new_file_write = os.path.join(os.path.dirname(__file__), "file_5_4_2.txt")

translation = {'One' : 'Один',
               'Two' : 'Два',
               'Three' : 'Три',
               'Four' : 'Четыре'}
# print(translation)
new_data = []

with open(my_file_read, 'r', encoding="UTF-8") as my_file:
    for itm in my_file:
        itm = itm.split(" ", 1)
        new_data.append(translation[itm[0]] + ' ' + itm[1])
    print(new_data)

with open(new_file_write, 'w', encoding="UTF-8") as new_file:
    new_file.writelines(new_data)
