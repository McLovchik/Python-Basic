def rollover(rollover__word):
    return rollover__word[::-1]


def check_is_alpha(check_is_alpha__word):
    if check_is_alpha__word.isalpha():
        return True


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

    # b = a[::-1]
    # a[len(a) - 1]
    # 'v'

message_split = ' '.join(message_split)

print(' '.join(new_message_split))
