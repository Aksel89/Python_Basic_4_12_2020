user_name = input("Введите ваше имя\n>>>")
user_age = input("Введите свой возраст\n>>>")

if user_age.isdigit():
    user_age = int(user_age)
else:
    print(user_name, "Ошибка ввода возраста, введите число")
    exit()

print("Добрый вечер", user_name, sep=",")
# system_message = "Пользователь {name} в возрасте {age} лет вошел в систему".format(name = user_name, age = user_age)
system_message = f"Пользователь {user_name} в возрасте {user_age} лет вошел в систему"
print(system_message)
if user_age >= 18:
    print("Доступ разрешен в ХХХ")
elif user_age >= 16:
    print("Доступ к боевикам")
else:
    print("Ограниченный доступ")

print("Отсчет возраста")

temp_age = user_age
while temp_age > 0:
    if not temp_age & 1:
        temp_age -= 1
        continue
    print(temp_age)
    # if temp_age = 15:
    # break
    temp_age = temp_age - 1
    temp_age -= 1
else:
    print("Сработал else цикла")
