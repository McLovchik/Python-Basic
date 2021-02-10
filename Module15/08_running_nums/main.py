def copy_fun(array, quantity_elements):
    new_fun = []
    for ind in range(quantity_elements):
        new_fun.append(array[ind])
    return new_fun


shift = int(input('Сдвиг: '))
elements = int(input('Сколько элементов в списке: '))
initial_list = []
var_list = []

print('Введите элементы списка по одному')

for _ in range(elements):
    element = int(input(''))
    initial_list.append(element)
    var_list.append(0)

print('Изначальный список:', initial_list)

for _ in range(shift):
    for index in range(elements):
        var_list[-index] = initial_list[elements - index - 1]
    initial_list = copy_fun(var_list, elements)

print('Сдвинутый список:', var_list)
