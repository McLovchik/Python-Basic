def check_upper_digit(user_password):
    list_pass = list(user_password)
    count_numbers = 0
    count_upper = 0
    for letter in list_pass:
        if letter.isdigit():
            count_numbers += 1
        if letter.isupper():
            count_upper += 1
    if count_numbers >= 3 and count_upper >= 1:
        return True


while True:
    password = input('Придумайте пароль: ')
    if len(password) >= 8 and check_upper_digit(password):
        break
    print('Пароль ненадёжный. Попробуйте ещё раз.')

print('Это надёжный пароль!')
