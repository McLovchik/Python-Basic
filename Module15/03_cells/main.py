number_of_cells = int(input('Кол-во клеток: '))
list_efficiency = []

for number in range(1, number_of_cells + 1):
    efficiency = int(input(f'Эффективность {number} клетки: '))
    list_efficiency.append(efficiency)

print('Неподходящие значения:', end=' ')

for number in range(1, number_of_cells + 1):
    if list_efficiency[number - 1] < number:
        print(list_efficiency[number - 1], end=' ')
