# Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и
# вычисляет общее количество строк кода, игнорируя пустые строки и строчки комментариев.

import os


def counter_str(fun_path: str):
    for elem in os.listdir(fun_path):
        strings = 0
        new_path = os.path.abspath(os.path.join(fun_path, elem))
        if os.path.isfile(new_path):
            if new_path.endswith('.py'):
                with open(new_path) as file:
                    read_file = file.read().split('\n')
                    for i_str in read_file:
                        if i_str.strip() and not i_str.startswith('#') and not i_str.startswith('"') \
                                and not i_str.startswith("'"):
                            strings += 1
                    yield strings
        elif os.path.isdir(new_path) and not os.path.isfile(new_path):
            yield from counter_str(new_path)


# path = 'C:\\Users\\McLovchik\\PycharmProjects\\chisl\\New_ch'
path = input('Введите путь: ')

sum_str = 0
for i in counter_str(path):
    sum_str += i
print(sum_str)
