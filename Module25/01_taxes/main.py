class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 500


def is_enough(fun_money, fun_tax):
    if fun_money >= fun_tax:
        print('Денег хватает')
    else:
        print('Не хватает', fun_tax - fun_money)


money = int(input('Сколько у вас денег? '))
choice = int(input('Какое имущество? (1 - квартира, 2 - машина, 3 - дача) --- '))
property_value = int(input('Введите стоимость имущества: '))


if choice == 1:
    calculated_tax = Apartment(property_value).tax_calculation()
    print('Налог на кваритру:', calculated_tax)
    is_enough(money, calculated_tax)
elif choice == 2:
    calculated_tax = Car(property_value).tax_calculation()
    print('Налог на машину:', calculated_tax)
    is_enough(money, calculated_tax)
elif choice == 3:
    calculated_tax = CountryHouse(property_value).tax_calculation()
    print('Налог на дачу:', calculated_tax)
    is_enough(money, calculated_tax)
