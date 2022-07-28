with open('people.txt', 'r', encoding='utf-8') as people_file:
    name_line = people_file.read().split('\n')
    res = ''.join(name_line)
    try:
        for number, name in enumerate(name_line):
            if len(name) < 3:
                raise ValueError(f'Ошибка: менее трёх символов в строке {number+1}')
    except ValueError:
        print(f'Ошибка: менее трёх символов в строке {number+1}')
    finally:
        print(f'Общее количество символов: {len(res)}')
