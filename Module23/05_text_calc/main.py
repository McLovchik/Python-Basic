operations = ['*', '/', '+', '-', '%', '//']
our_sum = 0


def if_error(example_list):
    correct_mistake = input(f'Обнаружена ошибка в строке: {example_list}  Хотите исправить? ')
    if correct_mistake.lower() == 'да':
        new_operation = input('Введите исправленную строку: ').split()
        return new_operation
    else:
        return False


def check_int(number):
    if float(number) % int(number) == 0:
        return True
    else:
        return False


with open('calc.txt', 'r') as calc_file:
    data = calc_file.read()
    exx = data.split('\n')
    for i_ex in exx:
        ex_list = i_ex.split()
        if ex_list[0] == '-':
            del ex_list[0]
            ex_list[0] = '-' + ex_list[0]
        if len(ex_list) != 3:
            if_error_value = if_error(ex_list)
            if if_error_value:
                ex_list = if_error_value
                join_ex_list = ''.join(ex_list)
                our_sum += eval(join_ex_list)
        elif not check_int(ex_list[0]) or not check_int(ex_list[2]):
            if_error_value = if_error(ex_list)
            if if_error_value:
                ex_list = if_error_value
                join_ex_list = ''.join(ex_list)
                our_sum += eval(join_ex_list)
        elif ex_list[1] not in operations:
            if_error_value = if_error(ex_list)
            if if_error_value:
                ex_list = if_error_value
                join_ex_list = ''.join(ex_list)
                our_sum += eval(join_ex_list)
        else:
            join_ex_list = ''.join(ex_list)
            our_sum += eval(join_ex_list)

print('Сумма результатов:', our_sum)
