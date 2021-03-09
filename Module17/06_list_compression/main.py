count_numbers = int(input('Кол-во чисел: '))
print('Введите сами числа')
numbers_list = [int(input()) for _ in range(count_numbers)]

# TODO: Отсутствет шаг с нулями в конце:(
for _ in range(numbers_list.count(0)):
    numbers_list.remove(0)

print(numbers_list)
