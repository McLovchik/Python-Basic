def out_of_num(num, temp=1):
    if temp < num:
        print(temp)
        out_of_num(num, temp + 1)
    else:
        print(num)


number = int(input('Введите число: '))
out_of_num(number)
