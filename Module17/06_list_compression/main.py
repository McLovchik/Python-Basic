count_numbers = int(input('Кол-во чисел: '))
print('Введите сами числа')
numbers_list = [int(input()) for _ in range(count_numbers)]

for _ in range(numbers_list.count(0)):
    numbers_list.remove(0)

print(numbers_list)
