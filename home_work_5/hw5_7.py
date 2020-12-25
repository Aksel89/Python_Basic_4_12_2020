"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import os
import json

my_file = os.path.join(os.path.dirname(__file__), "file_5_7.txt")
my_file_js = os.path.join(os.path.dirname(__file__), "file_5_7.json")


firms = {}
profit_firms = {}
profit = 0
aver_profit = 0
numbers_firm = 0

with open(my_file, 'r', encoding='UTF-8') as file:
    for line in file:
        name, firm, revenue, costs = line.split()
        firms[name] = int(revenue) - int(costs)
        if firms.setdefault(name) >= 0:
            profit = profit + firms.setdefault(name)
            numbers_firm += 1
    if numbers_firm != 0:
        aver_profit = profit / numbers_firm
        print(f'Средняя прибыль: {aver_profit:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    profit_firms = {'средняя прибыль': round(aver_profit)}
    firms.update(profit_firms)
    print(f'Прибыль каждой фирмы - {firms}')

with open(my_file_js, 'w') as write_js:
    json.dump(firms, write_js)

    js_str = json.dumps(firms)
    print(f'Создан файл json с содержимым: \n '
          f' {js_str}')

