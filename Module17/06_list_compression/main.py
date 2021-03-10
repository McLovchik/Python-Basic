count_numbers = int(input('Кол-во чисел: '))
print('Введите сами числа')
numbers_list = [int(input()) for _ in range(count_numbers)]

for i_index in range(count_numbers - 1):
    for i_index_two in range(i_index + 1, count_numbers):
        if numbers_list[i_index] == 0 and numbers_list[i_index_two] != 0:
            numbers_list[i_index], numbers_list[i_index_two] = numbers_list[i_index_two], numbers_list[i_index]
            break

print(numbers_list)

for _ in range(numbers_list.count(0)):
    numbers_list.remove(0)

print(numbers_list)
