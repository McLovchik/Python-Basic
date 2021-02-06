containers = int(input('Кол-во контейнеров: '))
weights = []

for _ in range(containers):
    while True:
        print('Введите вес контейнера:', end=' ')
        added_weight = float(input())
        if added_weight - int(added_weight) == 0 and added_weight <= 200:
            weights.append(added_weight)
            break
        else:
            print('Все числа целые и не превышают 200')

print()

while True:
    weight_new_c = float(input('Введите вес нового контейнера: '))
    if weight_new_c - int(weight_new_c) == 0 and weight_new_c <= 200:
        break

print()

count = 0
for number in range(containers):
    if weight_new_c > weights[number]:
        print('Номер, куда встанет новый контейнер: ', number + 1)
        count += 1
        break

if count == 0:
    print('Номер, куда встанет новый контейнер: ', containers + 1)
