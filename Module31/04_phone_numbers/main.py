user_list = ['9999999999', '999999-999', '99999x9999']

for number in user_list:
    if number.startswith(('8', '9')) and len(number) == 10 and all(map(str.isdigit, number)):
        print(f'{number} - всё в порядке')
    else:
        print(f'{number} - не подходит')
