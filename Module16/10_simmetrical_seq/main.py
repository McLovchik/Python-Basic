def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


numbers_list = []
numbers = int(input('Кол-во чисел: '))

for i_index in range(1, numbers + 1):
    num = int(input(f'Число {i_index}: '))
    numbers_list.append(num)

new_numbers_list = []
answer = []

for i_nums in range(0, len(numbers_list)):
    for j_elem in range(i_nums, len(numbers_list)):
        new_numbers_list.append(numbers_list[j_elem])
    if is_palindrome(new_numbers_list):
        for i_answer in range(0, i_nums):
            answer.append(numbers_list[i_answer])
        answer.reverse()
        break
    new_numbers_list = []

print('Исходный список:', numbers_list)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)
