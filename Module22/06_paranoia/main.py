import os


def caesar_cipher(fun_string, var_shift, alphabet='abcdefghijklmnopqrstuvwxyz'):
    char_list = [
        (alphabet[(alphabet.index(symbol) + var_shift) % 26]
         if symbol != ' ' else ' ')
        for symbol in fun_string
    ]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


name_file = 'text.txt'
path_to_txt = os.path.abspath(name_file)
file_contents = open(path_to_txt, 'r')
data = file_contents.read()
data_list = data.split('\n')

count = 0
caesar_cipher_data_list = []
for i_str in data_list:
    count += 1
    caesar_cipher_str = caesar_cipher(i_str.lower(), count)
    caesar_cipher_data_list.append(caesar_cipher_str.capitalize())

file_contents.close()

path_to_new_file = os.path.abspath(os.path.join(path_to_txt, '..', 'cipher_text.txt'))
cipher_text = open(path_to_new_file, 'w')
for j_str in range(len(caesar_cipher_data_list)):
    if j_str != len(caesar_cipher_data_list) - 1:
        cc_str = caesar_cipher_data_list[j_str] + '\n'
    else:
        cc_str = caesar_cipher_data_list[j_str]
    cipher_text.write(cc_str)

cipher_text.close()
