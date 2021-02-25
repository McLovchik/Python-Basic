main = [1, 5, 3]
first_s = [1, 5, 1, 5]
second_s = [1, 3, 1, 5, 3, 3]

amount_main = len(main)

main.extend(first_s)
print('Кол-во цифр 5 при первом объединении:', main.count(5))

for _ in range(len(main) - 1, amount_main, -1):
    main.remove(5)

main.extend(second_s)
print('Кол-во цифр 3 при втором объединении:', main.count(3))

print(main)

