count = int(input('Введите кол-во заказов: '))

orders_dict = dict()

for i_order in range(1, count + 1):
    order = input(f'{i_order} заказ: ').split()
    if order[0] not in orders_dict:
        orders_dict[order[0]] = list()
        orders_dict[order[0]].append({order[1]: int(order[2])})
    elif order[1] not in orders_dict[order[0]][0]:
        orders_dict[order[0]].append({order[1]: int(order[2])})
    elif order[0] in orders_dict:
        if order[1] not in orders_dict[order[0]][0]:
            orders_dict[order[0]].append({order[1]: int(order[2])})
        elif order[1] in orders_dict[order[0]][0]:
            orders_dict[order[0]][0][order[1]] += int(order[2])

print()
for i_key in orders_dict:
    print(f'{i_key}:')
    for j_key in orders_dict[i_key]:
        print(j_key)

