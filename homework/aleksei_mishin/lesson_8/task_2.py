# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

import sys

sys.set_int_max_str_digits(100000)


def fibonacci_seq_generator():
    prev1 = -1
    prev2 = 1
    cur = 0

    while True:
        cur = prev1 + prev2
        yield cur
        prev1, prev2 = prev2, cur


def get_fibonacci_number(position):
    cnt = 1
    result = None
    position = 1 if (position == 0 or position < 0) else position

    for num in fibonacci_seq_generator():
        if cnt == position:
            result = num
            break

        cnt += 1

    return result


print(get_fibonacci_number(5))
print(get_fibonacci_number(200))
print(get_fibonacci_number(1000))
print(get_fibonacci_number(100000))
