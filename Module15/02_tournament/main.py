list_names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
list_names_2nd = []

for number in range(0, len(list_names), 2):
    list_names_2nd.append(list_names[number])

print('Элементы списка только с чётными индексами:', list_names_2nd)
