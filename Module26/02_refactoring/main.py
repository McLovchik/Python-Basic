# Нужно найти, какие два числа из списков в результате попарного перемножения дадут число 56.

to_find = 56


def gen():
    list_1 = [2, 5, 7, 10]
    list_2 = [3, 8, 4, 9]
    for fun_x in list_1:
        for fun_y in list_2:
            yield fun_x, fun_y, fun_x * fun_y


for x, y, result in gen():
    print(x, y, result)
    if result == to_find:
        print('Found !!!')
        break
