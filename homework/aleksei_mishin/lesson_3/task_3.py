import math


# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

def average(a, b):
    return a + b / 2


def geometric_average(a, b):
    return math.sqrt((a * b))


print(average(10, 50))
print(geometric_average(8, 8))
