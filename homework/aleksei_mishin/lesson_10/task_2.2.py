# # Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор,
# # который сможет обработать такой код:
# #
# # @repeat_me(count=2)
# # def example(text):
# #     print(text)
# #
# # example('print me')


def repeat_me(count=1):
    def decorator(func):
        def wrapper(text):
            for _ in range(count):
                func(text)

        return wrapper

    return decorator


@repeat_me(count=2)
def print_text(text):
    print(text)


print_text("Hello world!")
