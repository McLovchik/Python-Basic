# TODO: Не очень правильно внутри ф-ии использовать имена переменных такие же как и в глобальной области видимости:
#  предлагаю переименовать:)
def check(begin_list, end_list, file_name):
    # TODO: Предлагаю сделать правильнее и проще:
    #  проверяйте первый символ на вхождение в строку с запрещенными символами при помощи оператора "in":)
    for elem in begin_list:
        if file_name.startswith(elem):
            print('Ошибка: название начинается на один из специальных символов')
            return False

    for elem_two in end_list:
        if file_name.endswith(elem_two):
            return True

    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    return False


# TODO: Есть ли необходимость в преобразовании в список?:)
begin_list = list('@№\$%^&*()')
end_list = ['.txt', '.docx']

name = input('Название файла: ')

if check(begin_list, end_list, name):
    print('Файл назван верно.')

# Всё таки методы нельзя отправлять в функции?
# TODO: Только с самим объектом, над которым метод будет выполнен:)
