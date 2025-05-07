# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция
#
# Код, использующий этот декоратор может выглядеть, например, так:
#
# @repeat_me
# def example(text):
#     print(text)
#
# example('print me', count=2)
# В результате работы будет такое:
#
# print me
#
# print me


def repeat_me(func):
    def wrapper(text, count=1):
        for i in range(count):
            func(text)

    return wrapper


@repeat_me
def print_text(text):
    print(text)


print_text("Hello world!", count=2)
