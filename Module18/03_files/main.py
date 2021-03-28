def check_start(suspect, file_name):
    for elem in suspect:
        if file_name.startswith(elem):
            return True
    return False


def check_end(suspect, file_name):
    for elem in suspect:
        if file_name.endswith(elem):
            return True
    return False


begin_list = list('@№\$%^&*()')
end_list = ['.txt', '.docx']

name = input('Название файла: ')

if check_start(begin_list, name):
    print('Ошибка: название начинается на один из специальных символов')
elif not check_end(end_list, name):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')

# Можно ли отправить функцию в другую создаваемую функцию, чтобы не нарушалось правило dry
