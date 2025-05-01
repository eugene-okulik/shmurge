# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
#
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.

from random import random, choice


def give_bonus():
    salary = int(input("Укажите вашу зарплату: "))
    bonus = choice([True, False])
    final_salary = salary + int(salary * random()) if bonus else salary
    print(f"{salary}, {bonus} - '${final_salary}'")


give_bonus()
