def crypto(verifiable_list):
    return [j for i, j in enumerate(verifiable_list) if is_prime(i)]


def is_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False


text = input('Введите текст: ').split()
i_list = crypto(text)
print(i_list)

# как быть с вводом, я не понял. Нужно исп-ть tuple?
# и что значит основной код??
