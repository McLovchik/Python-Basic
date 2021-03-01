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

for elem in first_list:
    count = 0
    for elem_two in first_list:
        while elem == elem_two:
            count += 1
            break
    while count != 1:
        first_list.remove(elem)
        count -= 1

print('Новый первый список с уникальными элементами:', first_list)

# оказывается я плохо ценил прохождение цикла сразу по элемантам)
# применив такой метод, сразу всё получилось, спасибо)
# TODO: Это действительно удобно! Всегда пожалуйста!
#  p.s. количество конкретных элементов в списке можно получать при помощи метода count() ;)
