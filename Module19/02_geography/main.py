def check_value(our_dict, value):
    for k in our_dict.keys():
        for v in our_dict[k]:
            if v == value:
                return k


countries = int(input('Кол-во стран: '))

country_cities_dict = dict()

for i_country in range(1, countries + 1):
    country_cities = input(f'{i_country} страна: ').split()
    country_cities_dict[country_cities[0]] = country_cities[1::]

count = 1
while True:
    city = input(f'{count} город: ')
    if check_value(country_cities_dict, city):
        print(f'Город {city} расположен в стране {check_value(country_cities_dict, city)}.')
        count += 1
    else:
        print(f'По городу {city} данных нет.')
        break
