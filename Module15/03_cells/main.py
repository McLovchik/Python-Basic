number_of_cells = int(input('Кол-во клеток: '))
list_efficiency = []

for number in range(1, number_of_cells + 1):
    print('Эффективность', number, 'клетки:', end=' ')
    # TODO: Хотите научиться вставлять любой текст сразу в input?:)
    # Да, конечно!
    # TODO: Самым простым способом было бы использовать конкатенацию:
    #  efficiency = int(input('Эффективность' + str(number) + 'клетки:'))
    #  Однако есть еще несколько более профессиональных способов:
    #  1) оператор %
    #  efficiency = int(input('Эффективность %d клетки:' % number))
    #  2) метод format()
    #  efficiency = int(input('Эффективность {} клетки:'.format(number)))
    #  3) f-строки
    #  efficiency = int(input(f'Эффективность {number} клетки:'))
    # TODO: Предлагаю использовать любой из способов (кроме конкатенации)
    efficiency = int(input())
    list_efficiency.append(efficiency)

print('Неподходящие значения:', end=' ')

for number in range(1, number_of_cells + 1):
    if list_efficiency[number - 1] < number:
        print(list_efficiency[number - 1], end=' ')
