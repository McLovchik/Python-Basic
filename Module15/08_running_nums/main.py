shift = int(input('Сдвиг: '))
elements = int(input('Сколько элементов в списке: '))
initial_list = []
var_list = []
zero_list = []

print('Введите элементы списка по одному')

for _ in range(elements):
    element = int(input(''))
    initial_list.append(element)
    var_list.append(0)

zero_list = var_list

print('Изначальный список:', initial_list)

for _ in range(shift):
    for index in range(elements):
        var_list[-index] = initial_list[elements - index - 1]
    initial_list = var_list
    var_list = zero_list

print('Сдвинутый список:', initial_list)

