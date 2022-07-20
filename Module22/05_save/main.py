import os


def get_path(begin_dir, path_to_dir_list):
    for i_dir in path_to_dir_list:
        if os.path.exists(os.path.abspath(os.path.join(begin_dir, i_dir))):
            begin_dir = os.path.abspath(os.path.join(begin_dir, i_dir))
        else:
            return 'Указанный из папок путь не существует на диске'
    return begin_dir


def write_file(fun_file, write_text):
    file_contents = open(fun_file, 'w')
    file_contents.write(write_text)
    file_contents.close()


text = input('Введите строку: ')
user_path_list = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
root_dir = os.path.abspath(os.sep)
our_path = get_path(root_dir, user_path_list)

user_name = input('Введите имя файла: ') + '.txt'
path_to_file = os.path.abspath(os.path.join(our_path, user_name))
if os.path.exists(path_to_file):
    answer_overwrite = input('Вы действительно хотите перезаписать файл? ').lower()
    if answer_overwrite == 'да':
        write_file(path_to_file, text)
        print('Файл успешно перезаписан!')
    elif answer_overwrite == 'нет':
        print('Ничего не произошло, файл не перезаписан')
else:
    write_file(path_to_file, text)
    print('Файл успешно сохранён!')
