def sort(elements, sort_list):
    for i_min_num in range(elements):
        for i_act in range(i_min_num, elements):
            if sort_list[i_act] < sort_list[i_min_num]:
                sort_list[i_act], sort_list[i_min_num] = sort_list[i_min_num], sort_list[i_act]
    return sort_list


skates_list = []
skates = int(input('Кол-во коньков: '))
for number in range(1, skates + 1):
    size = int(input(f'Размер {number} пары: '))
    skates_list.append(size)

print()

people_list = []
people = int(input('Кол-во людей: '))
for number in range(1, people + 1):
    size = int(input(f'Размер ноги {number} человека: '))
    people_list.append(size)

skates_list = sort(skates, skates_list)
people_list = sort(people, people_list)

count = 0
while len(people_list) != 0 and len(skates_list) != 0:
    if skates_list[0] >= people_list[0]:
        count += 1
        people_list.remove(people_list[0])
    skates_list.remove(skates_list[0])

print(count)
