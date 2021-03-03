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

# TODO: Аналогично 3;)
for i_elem in first_list:
    count = 0
    for i_elem_two in first_list:
        while i_elem == i_elem_two:
            count += 1
            break
    while count != 1:
        first_list.remove(i_elem)
        count -= 1

print('Новый первый список с уникальными элементами:', first_list)

# оказывается я плохо ценил прохождение цикла сразу по элемантам)
# применив такой метод, сразу всё получилось, спасибо)
# Это действительно удобно! Всегда пожалуйста!
# количество конкретных элементов в списке можно получать при помощи метода count() ;)
# да, правда, в следующий раз учту
