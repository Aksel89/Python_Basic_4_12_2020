"""DRY - don't repeat yorself - не повторяй себя"""

"""
Необходимо напечатать на экране YES, NO если переданное число имеет 3 цифры
"""

# def some(number):
#     answer = ('NO', 'YES')
#     print(answer[1 <= (number // 100) < 10])
#
# some(235)

def is_some(number: int, count: int) -> bool:
    """ Функция возвращает является ли число n разрядным
    :param number: int: Число
    :param count: int: Количество цифр в числе
    :return: bool
    """
    return 1 <= (number // 10 ** (count - 1)) < 10

# a = is_some(123, 3)
# b = is_some(123, 4)
# c = is_some(12, 5)
# d = is_some(123456, 6)
#
# print(any(a, b, c, d))

# print(is_some(count=5, number=34651 ))

# a = {
#     'count': 5,
#     'number': 2345,
# }
#
# b = [23456, 5]
#
# print(is_some(**a))
#
# print(is_some(*b))

"""
zip
map
reduce
filter
enumerate
range
sum
min
max
len
"""

# def my_map(funk, iter_obj):
#     result = []
#     for item in iter_obj:
#         result.append(funk(item))
#     return result

# def my_map(funk, iter_obj):
#     for item in iter_obj:
#         yield funk(item)
#
# a = my_map(str, [1, 2, 3, 4, 5])
#
# print(type(a))

def my_sum(*args, factor=1):
    result = 0
    for n in args:
        result += n
    return result * factor

print(my_sum(1, 2, 3, 4, 5, 6, 7))