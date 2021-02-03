a = int(input('Введите первый год: '))
b = int(input('Введите второй год: '))

for year in range(a, b + 1):
    same_year = year
    for number in range(0, 10):
        year = same_year
        count = 0
        while year != 0:
            if year % 10 == number:
                count += 1
            year //= 10
        if count == 3:
            print(same_year)
