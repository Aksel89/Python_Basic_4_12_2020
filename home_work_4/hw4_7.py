"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from my_funcs import fact


num = int(input("Для расчета факториала введите любое натуральное число>>>\n"))

# Формулировка не особо удачная, но не придумал как это правильнее и понятнее записать))
my_range = int(input("Введите натуральное число, но не больше введеного ранее, которое отвечает\n"
                     "за вывод количества первых элементов в расчете факториала >>>\n"))

factorial_num = fact(num)

for idx, el in enumerate(factorial_num, 1):
    if idx <= my_range:
        print(f"Первые {my_range} элемента(ов) {idx, el}")
