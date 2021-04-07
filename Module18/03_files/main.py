def check(start_list, back_list, file_name):
    if file_name[0] in start_list:
        print('Ошибка: название начинается на один из специальных символов')
        return False

    for elem_two in back_list:
        if file_name.endswith(elem_two):
            return True

    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    return False


begin_list = ('@№\$%^&*()')
end_list = ['.txt', '.docx']

name = input('Название файла: ')

if check(begin_list, end_list, name):
    print('Файл назван верно.')
