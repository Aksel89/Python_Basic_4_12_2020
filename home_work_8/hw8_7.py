'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 'a + b * j'

    def __add__(self, other):
        print(f'Сумма комплексных чисел:')
        return f'c = {self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел:')
        return f'c = {self.a * other.a - self.b * other.b} + {self.a * other.b + other.a * self.b} * j'

    def __str__(self):
        return f'c = {self.a} + {self.b} * j'


num1 = ComplexNumbers(5, 8)
num2 = ComplexNumbers(7, -6)
print(num1)
print(num2)
print(num1 + num2)
print(num1 * num2)