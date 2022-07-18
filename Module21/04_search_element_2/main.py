site = {
    'html': {                                       # 1
        'head': {                                   # 2
            'title': 'Мой сайт'                     # 3
        },
        'body': {                                   # 2
            'h2': 'Здесь будет мой заголовок',      # 3
            'div': 'Тут, наверное, какой-то блок',  # 3
            'p': 'А вот здесь новый абзац'          # 3
        }
    }
}


def find_key(struct, key, depth):
    if depth is None or depth >= 1:
        if key in struct:
            return struct[key]
    else:
        return None

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, depth - 1 if isinstance(depth, int) else depth)
            if result:
                break
    else:
        result = None

    return result


user_key = input('Введите искомый ключ: ')
user_depth_y_or_n = input('Хотите ввести максимальную глубину? Y/N: ').lower()
user_depth = None
if user_depth_y_or_n == 'y':
    user_depth = int(input('Введите максимальную глубину: '))

value = find_key(site, user_key, user_depth)
print(value)
