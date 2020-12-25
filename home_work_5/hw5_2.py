"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os
import re


my_file = os.path.join(os.path.dirname(__file__), "file_5_2.txt")

itr = 0
with open(my_file, "r", encoding="UTF-8") as file:
    #words = len(re.findall(r'\w+', file.readline()))
    #count_str = sum(1 for line in file)
    #print(count_str)
    # # print(words)
    #while itr <= count_str:


    for line in file:
        for words in line:
            words = len(re.findall(r'\w+', file.readline()))
        #itr += 1
            print(words)


