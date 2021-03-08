text = input('Введите текст: ')
symbols_text = list(text)
for i_index in range(len(symbols_text)):
    if symbols_text[i_index] == 'h':
        left_index = i_index
        break

reverse_symbol_text = symbols_text[::-1]
for i_index in range(len(reverse_symbol_text)):
    if reverse_symbol_text[i_index] == 'h':
        right_index = i_index
        break
right_index = len(symbols_text) - right_index - 1

symbols_text[left_index:right_index + 1] = symbols_text[right_index:left_index - 1:-1]

print(symbols_text)
