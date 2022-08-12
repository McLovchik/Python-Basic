from typing import Callable

app = {}


def callback(fun_route: str):
    """Функция обратного вызова, вызывается при срабатывании события"""

    def wrapped(func: Callable) -> Callable:
        app[fun_route] = func

        def wrapper():
            ret = func()
            return ret

        return wrapper

    return wrapped


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
