def create_list(name, num, d_list):
    print(f'{name} список из {num} чисел')
    for _ in range(num):
        number = input()
        d_list.append(number)


first_list = []
create_list('Первый', 3, first_list)

second_list = []
create_list('Второй', 7, second_list)

first_list.extend(second_list)
i_index = 0
# TODO: Предлагаю подумать над более оптимальным алгоритмом:)
while i_index <= len(first_list) - 2:
    i_index_two = i_index + 1
    while i_index_two <= len(first_list) - 1:
        while first_list[i_index] == first_list[i_index_two]:
            first_list.remove(first_list[i_index_two])
            i_index_two -= 1
            while i_index != 0:
                i_index -= 1
            break
        i_index_two += 1
    i_index += 1

print('Новый первый список с уникальными элементами:', first_list)
