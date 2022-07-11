def first_choice(contacts_dict):
    name_surname = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    name_surname = tuple(name_surname)
    if name_surname in contacts_dict.keys():
        print('Такой человек уже есть в контактах.')
    else:
        number = int(input('Введите номер телефона: '))
        contacts_dict[name_surname] = number
    print('Текущий словарь контактов:', contacts_dict)


def second_choice(contacts_dict):
    surname_for_search = input('Введите фамилию для поиска: ')
    for i_key in contacts_dict:
        if surname_for_search.capitalize() in i_key:
            print(i_key[0], i_key[1], contacts_dict[i_key])
            break


contacts = dict()

while True:
    print('Введите номер действия: ')
    print(' 1. Добавить контакт ')
    print(' 2. Найти человека ')
    choice = int(input(''))
    if choice == 1:
        first_choice(contacts)
    elif choice == 2:
        second_choice(contacts)
