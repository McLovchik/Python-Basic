people = int(input('Кол-во человек: '))
people_list = list(range(1, people + 1))
drop_out = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', drop_out, 'человек')
print()

start = 0
while len(people_list) != 1:
    print('Текущий круг людей:', people_list)
    print('Начало счёта с номера', people_list[start])
    retired = drop_out - len(people_list) - 1 + start
    while retired >= len(people_list):
        retired -= len(people_list)
    print('Выбывает человек под номером', people_list[retired])
    people_list.remove(people_list[retired])
    start = retired
    while start == len(people_list):
        start = 0
    print()

print('Остался человек под номером', people_list[0])
