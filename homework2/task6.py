"""
*Реализовать структуру данных «Товары».Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

# Это задание можно не оценивать. Я его сделал по Вашему образу. Разбирая все по действиям
# и записывая вручную в тетрадь. До некоторых вещей нне догадался сам.

product_parametrs = {
    "название": ('наименование товара', str),
    "цена": ('стоимость товара', int),
    "количество": ('количество', int),
    "ед": ('Единицы измерения (шт, кг, литр, прочее)', str),
}

next_enter = True
product_list = []
serial_number = 1

while next_enter:
    product = {}
    for key, value in product_parametrs.items():
        while True:
            add_product = input(f"Введите {value[0]}: ")
            try:
                add_product = value[1](add_product)
            except ValueError as e:
                print(f'{e}. Не верное значение')
                continue
            product[key] = add_product
            break
    product_list.append((serial_number, product))
    serial_number += 1

    while True:
        next_add = input("Добавить еще товар? Да/Нет. ")
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print("Неверный ввод. Повторите еще раз ")

print(product_list)
