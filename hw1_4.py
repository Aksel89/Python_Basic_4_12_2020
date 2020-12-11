"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

# Каюсь, пришлось подсмотреть, но как происходят все манипуляции понял.

while True:
    number = input("Введите число: ")
    if number.isdigit():
        number = int(number)
        break
    else:
        print("Это не число! введите число: ")

desired_number = 0
while number and desired_number !=9:
    temp = number % 10
    if temp > desired_number:
        desired_number = temp

    number //= 10

print(desired_number)
