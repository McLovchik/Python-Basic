text = input('Введите текст: ')
symbols_text = list(text)
for i_index in range(len(symbols_text)):
    if symbols_text[i_index] == 'h':
        left_index = i_index
        break

reverse_symbol_text = symbols_text[::-1]

# Наверное right_index лучше создавать заранее. Если в строке нет h, получим ошибку.
for i_index in range(len(reverse_symbol_text)):
    if reverse_symbol_text[i_index] == 'h':
        right_index = i_index
        break
right_index = len(symbols_text) - right_index - 1

symbols_text[left_index + 1:right_index] = symbols_text[right_index - 1:left_index:-1]

print('Ответ: ', end='')

for symbol in symbols_text:
    print(symbol, end='')

# зачёт!