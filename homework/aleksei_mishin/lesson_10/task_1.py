# Создайте универсальный декоратор, который можно будет применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать слово "finished" после выполнения декорированной функции.
#
# Код, использующий этот декоратор может выглядеть, например, так:
#
# @finish_me
# def example(text):
#     print(text)
#
# example('print me')
# В результате работы будет такое:
#
# print me
#
# finished


def finish_me(func):
    def wrapper(text):
        func(text)
        print("finished")

    return wrapper


@finish_me
def print_text(text):
    print(text)


print_text("Let's started")
