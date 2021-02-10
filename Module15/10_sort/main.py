initial_list = []
elements = int(input('Сколько элементов в списке: '))

print('Введите элементы списка по одному')

for _ in range(elements):
    element = int(input(''))
    initial_list.append(element)

print('Изначальный список:', initial_list)

for min_num in range(elements):
    for act in range(min_num, elements):
        if initial_list[act] < initial_list[min_num]:
            initial_list[act], initial_list[min_num] = initial_list[min_num], initial_list[act]

print('Отсортированный список:', initial_list)
