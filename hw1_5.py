"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы
в расчете на одного сотрудника.
"""

while True:
    income = input("Введите вашу выручку: ")
    if income.isdigit():
        income = int(income)
        break
    else:
        print("Выручку необходимо указывать числом. Повторите ввод: ")

while True:
    cost = input("Введите ваши издержки: ")
    if cost.isdigit():
        cost = int(cost)
        break
    else:
        print("Издержки необходимо указывать числом. Повторите ввод: ")

financial_result = income - cost

if financial_result > 0:
    profit = income / cost
    print(f"Прибыль составила {financial_result}, рентабельность {profit}")
    while True:
        workers = input("Введите количество сотрудников: ")
        if workers.isdigit():
            workers = int(workers)
            break
        print("Количество сотрудников необходимо указать цифрой: ")
    profit_worker = financial_result / workers
    print(f"Прибыль на одного сотрудника составила {profit_worker}")

else:
    print(f"Выши убытки составили {financial_result}")
