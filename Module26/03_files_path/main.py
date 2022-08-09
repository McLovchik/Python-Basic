import os
from collections.abc import Iterable


def gen_files_path(folder: str, path: str) -> Iterable[str]:
    print('\n', 'Текущая директория', path)
    for i_elem in os.listdir(path):
        current_path = os.path.join(path, i_elem)
        if os.path.isdir(current_path) and i_elem != folder:
            yield from gen_files_path(folder, current_path)
        elif i_elem == folder:
            print('\n', 'Папка найдена!')
            print(current_path)
            break


user_folder = input('Введите название каталога: ')
abs_path = input('Введите также путь, откуда начать: ')
result = gen_files_path(folder=user_folder, path=abs_path)
for i_path in result:
    print(i_path)
