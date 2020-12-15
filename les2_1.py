"""
Неизменяемые данные
float
bool

None

str
tuple
frozenset

Изменяемые
list

dict
set


"""

some = 'sdfglijdlsakgffdflkg'

for char in some:
    print(char)

# idx = 0
# while idx < len(some):
#     item = some[idx]
#     print(item)
#     idx += 1      то же что и цикл FOR

some_list = [1, 2, 3, 'some string', True, 22.3]

some_dict = {
    'one': 1652,
    'two': 357336,
    'user_name': 'Some name',
    'user_age': 22,
}
