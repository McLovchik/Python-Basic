shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')
summa_money = 0
summa_det = 0

for i_index in range(0, len(shop)):
        if shop[i_index][0] == detail:
                summa_money += shop[i_index][1]
                summa_det += 1

print('Кол-во деталей -', summa_det)
print('Общая стоимость -', summa_money)