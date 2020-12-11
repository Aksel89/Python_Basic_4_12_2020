"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

name_dog = 'Jack'
age_dog = 7

print('Собаку зовут ', name_dog, 'ему ', age_dog, 'лет')

while True:
    city_name = input("Введите название города: ")
    if city_name.isalpha():
        city_name = str(city_name)
        break
    print('Ошибка, введите буквенное названние города: ')

while True:
    city_population = input("Введите количество жителей в городе: ")
    if city_population.isdigit():
        city_population = int(city_population)
        break
    print("Ошибка, введите число: ")

print(f"Я живу в городе {city_name}, в котором проживает еще {city_population} людей")
