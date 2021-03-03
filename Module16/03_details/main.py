shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')

sum_money = 0
sum_details = 0

for i_element in shop:
    if i_element[0] == detail:
        sum_money += i_element[1]
        sum_details += 1

print('Кол-во деталей -', sum_details)
print('Общая стоимость -', sum_money)
