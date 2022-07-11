data = {
    ('Петров', 'Андрей'): 36,
    ('Сидоров', 'Никита'): 35,
    ('Иванова', 'Маша'): 27,
    ('Сидорова', 'Алина'): 34,
    ('Петрова', 'Женя'): 33,
    ('Козлов', 'Семён'): 43,
    ('Сидоров', 'Павел'): 10,
}

input_surname = input('Введите фамилию: ').capitalize()
if input_surname.endswith('а'):
    is_woman = True
else:
    is_woman = False

if is_woman:
    for i_key in data.keys():
        if i_key[0] == input_surname or i_key[0] == input_surname[:-1]:
            print(i_key[0], i_key[1], data[i_key])
else:
    for i_key in data.keys():
        if i_key[0] == input_surname or i_key[0] == (input_surname + 'а'):
            print(i_key[0], i_key[1], data[i_key])
