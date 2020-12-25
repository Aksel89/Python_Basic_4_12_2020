"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os
import random

new_file_write = os.path.join(os.path.dirname(__file__), "file_5_5.txt")
random_nums = [random.randint(1, 1000) for _ in range(random.randint(5, 20))]
print(random_nums)

with open(new_file_write, 'w', encoding='UTF-8') as file:
    write_nums = ' '.join(map(str, random_nums))
    file.write(write_nums)


with open(new_file_write, 'r', encoding='UTF-8') as file:
    numbers = map(int, file.read().split(' '))

print(sum(numbers))
