n = float(input('Первое число: '))
k = float(input('Второе число: '))


def reverse(number):
    reverse_number = 0
    while number != 0:
        reverse_number = reverse_number * 10 + number % 10
        number //= 10
    return reverse_number


n_reverse_int = reverse(int(n))
k_reverse_int = reverse(int(k))

n_reverse_float = reverse(round(n - int(n), 2) * 100)
k_reverse_float = reverse(round(k - int(k), 2) * 100)

n_reverse = n_reverse_int + (n_reverse_float / 100)
k_reverse = k_reverse_int + (k_reverse_float / 100)

print('Первое число наоборот:', n_reverse)
print('Второе число наоборот:', k_reverse)
print('Сумма:', n_reverse + k_reverse)
