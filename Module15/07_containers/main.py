containers = int(input('Кол-во контейнеров: '))
weights = []


def check(the_weight):
    if the_weight - int(the_weight) == 0 and the_weight <= 200:
        return True


for _ in range(containers):
    while True:
        print('Введите вес контейнера:', end=' ')
        added_weight = float(input())
        if check(added_weight):
            weights.append(added_weight)
            break
        else:
            print('Все числа целые и не превышают 200')

print()

while True:
    weight_new_c = float(input('Введите вес нового контейнера: '))
    if check(weight_new_c):
        break
    else:
        print('Все числа целые и не превышают 200')
print()

count = 0
for number in range(containers):
    if weight_new_c > weights[number]:
        # Предлапгаю подумать, как избавиться от дублирования...
        # А где это дублирование?
        # TODO: Так я  же указал в прошлом сообщении. здесь и...
        print('Номер, куда встанет новый контейнер: ', number + 1)
        count += 1
        break


if count == 0:
    # ... да, это дублирования;)
    # TODO: ...здесь.
    #  У вас только отличаются предаваемые имена прменных (number  и containers),
    #  но в цеелом это дублирование кода, которого при желании можно избежать;)
    print('Номер, куда встанет новый контейнер: ', containers + 1)
