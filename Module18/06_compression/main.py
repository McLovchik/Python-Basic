message = input('Введите строку: ')
# aaAAbbсaaaA = a2A2b2a3A1

message_list = list(message)  # ['a', 'a', 'A', 'A', 'b', 'b', 'с', 'a', 'a', 'a', 'A']

new_list = []

i_number = 0
while i_number < len(message_list):
    count = 1
    new_list.append(message_list[i_number])
    for i_number_next in range(i_number + 1, len(message_list)):
        if message_list[i_number] == message_list[i_number_next]:
            count += 1
        else:
            break
    new_list.append(count)
    i_number += count

print('Закодированная строка: ', new_list)

# как объеденить?
