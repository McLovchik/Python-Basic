def create_list(name, num, d_list):
    print(f'{name} список из {num} чисел')
    for _ in range(num):
        number = int(input())
        d_list.append(number)
    return d_list


first_list = []
create_list('Первый', 3, first_list)

second_list = []
create_list('Второй', 7, second_list)

first_list.extend(second_list)

# не получается
# идею бы)
# TODO:
#  Проходитесь по элементам списка циклом for
#      Находите сколько штук данного элемеента в списке
#      Удаляйте это количество минус 1

print('Новый первый список с уникальными элементами:', first_list)
