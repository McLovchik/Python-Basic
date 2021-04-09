message = input('Сообщение: ')
message_split = message.split()

new_message_split = []

for word in message_split:
    if not word.isalpha():
        begin_index = 0
        var_full_word = []
        for i_symbol_index in range(len(word)):
            if word[begin_index:len(word)].isalpha():
                var_full_word.append((word[begin_index:len(word)])[::-1])
                break
            elif not word[i_symbol_index].isalpha():
                var_word = word[begin_index:i_symbol_index]
                var_word = var_word[::-1]
                var_word = ''.join([var_word, word[i_symbol_index]])
                var_full_word.append(var_word)
                begin_index = i_symbol_index + 1
        new_message_split.append(''.join(var_full_word))
    else:
        new_message_split.append(word[::-1])

print(' '.join(new_message_split))

# Сейчас кажется понятнее, а если делить на функции, то не очень удобно же, придется несколько переменных сувать
# в функцию
