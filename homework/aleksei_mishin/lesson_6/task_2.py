# Напишите программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3 она должна написать:
# "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz". Для чисел которые кратны одновременно и 3 и 5 надо
# печатать "FuzzBuzz". Иначе печатать число.


def fuzz_and_buzz_nums(start: int, stop: int):
    for i in range(start, stop + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FuzzBuzz")
        elif i % 3 == 0:
            print("Fuzz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fuzz_and_buzz_nums(1, 100)
