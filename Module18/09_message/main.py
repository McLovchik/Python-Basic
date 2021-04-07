# TODO: Есть ли необходимость в ф-ии, которая только возвращает срез?:)
def rollover(rollover__word):
    return rollover__word[::-1]


# TODO: Аналогично. Ф-ия по сути делает то же самое, что и метод isalpha().
def check_is_alpha(check_is_alpha__word):
    if check_is_alpha__word.isalpha():
        return True


# а если мне просто так удобнее было в данной задаче? и вроде понятность не теряется

message = input('Сообщение: ')
message_split = message.split()

new_message_split = []

for word in message_split:
    if not check_is_alpha(word):
        begin_index = 0
        var_full_word = []
        for i_symbol_index in range(len(word)):
            if word[begin_index:len(word)].isalpha():
                var_full_word.append(rollover(word[begin_index:len(word)]))
                break
            elif not word[i_symbol_index].isalpha():
                var_word = word[begin_index:i_symbol_index]
                var_word = rollover(var_word)
                begin_index = i_symbol_index + 1
                var_word = ''.join([var_word, word[i_symbol_index]])
                var_full_word.append(var_word)
        var_full_word = ''.join(var_full_word)
        new_message_split.append(var_full_word)
    else:
        word = rollover(word)
        new_message_split.append(word)

message_split = ' '.join(message_split)

print(' '.join(new_message_split))
# TODO: Не смотря на замечания выше предлагаю декомпозировать ф-ию :D (после их исправлений)
# и это обязательно ли, если мне так удобнее? и как мне кажется так будет хуже
