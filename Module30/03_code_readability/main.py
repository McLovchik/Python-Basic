my_list = [i for i in range(2, 1000) if 0 not in [i % j for j in range(2, i)]]

# print(my_list)


primes_list = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes_list.append(i)

# print(primes_list)
