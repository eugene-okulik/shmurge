import math


# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

def triangle_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def triangle_area(a, b):
    return (a * b) / 2


print(triangle_hypotenuse(6, 8))
print(triangle_area(6, 8))
