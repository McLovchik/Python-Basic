import os


def count_letters(data_file):
    cnt_letters = [i_elem for i_elem in data_file if i_elem.isalpha()]
    return len(cnt_letters)


def count_words(data_file):
    cnt_words = data_file.split(' ')
    # cnt_words = cnt_words.split('\n')
    print(cnt_words)
    return len(cnt_words)


def count_str(data_file):
    cnt_str = data_file.split('\n')
    return len(cnt_str)


path_file = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
readable_file = open(path_file, 'r')
data = readable_file.read().lower()


print('Количество букв в файле:', count_letters(data))
print('Количество слов в файле:', count_words(data) + (count_str(data) - 1) * 2)
print('Количество строк в файле:', count_str(data))
# Наиболее редкая буква:
