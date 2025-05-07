# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение


num_1 = float(input())
num_2 = float(input())


def get_operation(func):
    def wrapper(first_num, second_num, operation=None):
        if (first_num < 0) or (second_num < 0):
            operation = "*"
        elif first_num == second_num:
            operation = "+"
        elif first_num > second_num:
            operation = "-"
        elif first_num < second_num:
            operation = "/"

        return func(first_num, second_num, operation)

    return wrapper


@get_operation
def calc(first_num, second_num, operation=None):
    if operation == "+":
        return first_num + second_num
    elif operation == "-":
        return first_num - second_num
    elif operation == "/":
        return first_num / second_num
    elif operation == "*":
        return first_num * second_num


print(calc(num_1, num_2))
