n = int(input('Введите число: '))
list_odd = []

for number in range(1, n + 1):
    if number % 2 != 0:
        list_odd.append(number)

print('Список нечетных чисел:', list_odd)
