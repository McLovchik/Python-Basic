goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product in goods:
    for code in store:
        if goods[product] == code:
            price = 0
            count = 0
            for col in range(len(store[code])):
                price += store[code][col]['quantity'] * store[code][col]['price']
                count += store[code][col]['quantity']
            print(f'{product} - {count} шт, стоимость {price} руб')
            break
