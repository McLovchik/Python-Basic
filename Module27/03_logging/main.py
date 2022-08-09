from datetime import datetime
import functools


def logging(func):
    @functools.wraps(func)
    def wrapper_func():
        try:
            func()
            print(f'{func.__name__}:\n{func.__doc__}\n')
        except ValueError as exc:
            time = f'{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}'
            with open('function_errors.log', 'w', encoding='utf-8') as errors_file:
                errors_file.write(f'{func.__name__} - {exc} - {time}')
    return wrapper_func


@logging
def value_error():
    """ Value_error """
    flag = False
    if flag:
        print('5 + 5 = 11')
    else:
        raise ValueError('Ошибка значения')


@logging
def good_func():
    """ Good function """
    return 3


value_error()
good_func()
