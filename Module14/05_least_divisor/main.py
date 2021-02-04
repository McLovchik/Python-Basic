number = int(input('Введите число: '))

# TODO: Аналогично 3:)
def min_divider(number):
    for i in range(number, 1, -1):
        if number % i == 0:
            divider = i
    return divider

print('Наименьший делитель, отличный от единицы:',min_divider(number))