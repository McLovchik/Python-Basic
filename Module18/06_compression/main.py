message = input('Введите строку: ')
# aaAAbbсaaaA = a2A2b2a3A1

message_list = list(message)  # ['a', 'a', 'A', 'A', 'b', 'b', 'с', 'a', 'a', 'a', 'A']

new_list = []

i_number = 0
while i_number < len(message_list):
    count = 1
    new_list.append(message_list[i_number])
    i_number_next = i_number
    for i_number_next in range(i_number + 1, len(message_list)):
        # TODO: Предлагаю подумать как изменить ветвление ниже так чтобы оператор else был не нужен:)
        # я не догадался как(
        # TODO: Откатите код к прошлому решению прооверяйте не на равенство, а на неравенство.
        #  Если действительно не равно, то break и выход из цикла.
        #  Если нет, то выхода не произойдет и исполнится код дальше (увеличение счетчика)
        if message_list[i_number] == message_list[i_number_next]:
            count += 1
        else:
            break
    new_list.append(str(count))
    i_number += count


new_new_list = ''.join(new_list)
print('Закодированная строка: ', new_new_list)
