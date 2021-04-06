while True:
    ip = input('Введите IP: ')
    ip_list = ip.split('.')
    if len(ip_list) == 4 and ip.count('.') == 3:
        for number in ip_list:
            if not number.isdigit():
                print(number, '- не целое число')
                break
            elif int(number) > 255:
                print(number, 'превышает 255')
                break
        else:
            break
    else:
        print('Адрес - это четыре числа, разделенные точками')


print('IP-адрес корректен')
