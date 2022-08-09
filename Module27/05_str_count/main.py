from collections.abc import Callable
import functools


def counter(func: Callable) -> Callable:
    """ Декоратор, считающий и выводящий количество вызовов декорируемой функции """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} была вызвана: {wrapper.count} раз(-а)")
        return result
    wrapper.count = 0
    return wrapper


@counter
def test():
    print('TEST')


test()
test()
test()
