while True:
    count = 0
    ip = input('Введите IP: ')
    ip_list = ip.split('.')
    if len(ip_list) == 4:
        for number in ip_list:
            if not number.isdigit():
                print(number, '- не целое число')
                count += 1
                break
            elif int(number) > 255:
                print(number, 'превышает 255')
                count += 1
                break
    else:
        print('IP-адрес состоит из четырех чисел')
        count += 1
    if count == 0:
        break

print('IP-адрес корректен')
