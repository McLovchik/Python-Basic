import functools
from typing import Callable


def check_permission(user_name: str) -> Callable:
    """
    Декоратор для проверки прав пользователя.
    (Возвращает ошибку или право доступа к функции)
    """
    admin = ['admin']

    def check_permission_next(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Callable:
            try:
                if user_name in admin:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func_name}'.format(
                    func_name=func.__name__
                ))
        return wrapped
    return check_permission_next


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
