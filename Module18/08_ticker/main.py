first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')

first_str_list = list(first_str)
second_str_list = list(second_str)

for i_shift in range(len(first_str_list) - 1):
    var_for_first_list = first_str_list[-i_shift:] + first_str_list[:-i_shift]
    if var_for_first_list == second_str_list:
        print('Первая строка получается из второй со сдвигом', i_shift)
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
