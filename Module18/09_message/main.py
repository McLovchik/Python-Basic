def fun_if_part_of_word_is_not_alpha(fun_word, fun_begin_index, fun_i_symbol_index):
    fun_var_word = word[fun_begin_index:fun_i_symbol_index][::-1]
    fun_var_word = ''.join([fun_var_word, fun_word[fun_i_symbol_index]])
    return fun_var_word


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
                # var_word = word[begin_index:i_symbol_index][::-1]
                # var_word = ''.join([var_word, word[i_symbol_index]])
                var_full_word.append(fun_if_part_of_word_is_not_alpha(word, begin_index, i_symbol_index))
                begin_index = i_symbol_index + 1
        new_message_split.append(''.join(var_full_word))
    else:
        new_message_split.append(word[::-1])

print(' '.join(new_message_split))
