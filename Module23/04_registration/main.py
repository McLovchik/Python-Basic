file_out_good = open('registrations_good.log', 'w', encoding='utf-8')
file_out_bad = open('registrations_bad.log', 'w', encoding='utf-8')


def check_exceptions():
    if len(i_line) < 3:
        raise IndexError('НЕ присутствуют все три поля')
    elif not (str(name)).isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    elif mail.find('@') == -1 or mail.find('.') == -1:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
    elif not 10 <= int(age) <= 99:
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    file_out_good.write(i_line)


with open('registrations.txt', 'r', encoding='utf-8') as registration_file:
    for i_line in registration_file:
        try:
            name, mail, age = i_line.rstrip('\n').split(' ')
            check_exceptions()
        except IndexError as exc_i_e:
            file_out_bad.write(f'{name} {mail} {age}         {exc_i_e}\n')
        except NameError as exc_n_e:
            file_out_bad.write(f'{name} {mail} {age}         {exc_n_e}\n')
        except SyntaxError as exc_s_e:
            file_out_bad.write(f'{name} {mail} {age}         {exc_s_e}\n')
        except ValueError as exc_v_e:
            file_out_bad.write(f'{name} {mail} {age}         {exc_v_e}\n')


file_out_good.close()
file_out_bad.close()
