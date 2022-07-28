user_name = input('Как вас зовут? ')
while True:
    response = input('Введите 1, чтобы увидеть текущий текст чата или 2, чтобы написать сообщение: ')
    if response == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Служебное сообщение: пока ничего нет\n')
    elif response == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a') as file:
            file.write('{name}: {message}\n'.format(
                name=user_name, message=new_message
            ))
    else:
        print('Неизвестная команда\n')
