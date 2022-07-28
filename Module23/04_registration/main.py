file_out_good = 'registrations_good.log'
file_out_bad = 'registrations_bad.log'


def check_exceptions():
    if len(i_line) < 3:
        raise IndexError('НЕ присутствуют все три поля')
    elif not (str(name)).isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    elif mail.find('@') == -1 or mail.find('.') == -1:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
    elif not 10 <= int(age) <= 99:
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    with open(file_out_good, mode='a', encoding='utf-8') as file_good:
        file_good.write(i_line)


with open('registrations.txt', 'r', encoding='utf-8') as registration_file:
    for i_line in registration_file:
        try:
            name, mail, age = i_line.split(' ')
            check_exceptions()
        except (IndexError, NameError, SyntaxError, ValueError) as exc:
            with open(file_out_bad, mode='a', encoding='utf-8') as file_bad:
                file_bad.write(f"{i_line} _____ {exc} _____")

# как оформить нормальный вывод?
