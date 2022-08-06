import random


class FamilyMember:
    count_food = 0

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.degree_of_satiety = 30

    def is_dead_of_hunger(self):
        if self.degree_of_satiety <= 0:
            return True
        return False


class Person(FamilyMember):
    def __init__(self, name, house):
        super().__init__(name, house)
        self.degree_of_happiness = 100

    def pet_the_cat(self):
        print(f'{self.name} гладит кота')
        self.degree_of_happiness += 5
        self.degree_of_satiety -= 10

    def eating(self):
        if self.house.person_food >= 30:
            self.degree_of_satiety += 30
            self.count_food += 30
            self.house.person_food -= 30
            print(f'{self.name} поел(-а) на 30 единиц еды')
        elif self.house.person_food == 0:
            print(f'{self.name} не поел(-а)')
            print('Еда закончилась')
        else:
            self.degree_of_satiety += self.house.person_food
            self.count_food += self.house.person_food
            print(f'{self.name} опустошил(-а) весь холодильник, поел(-а) на {self.house.person_food} пункта')
            self.house.person_food = 0

    def happiness_falls_every_day(self):
        if self.house.is_dirty:
            self.degree_of_happiness -= 10

    def is_dead_of_depression(self):
        if self.degree_of_happiness < 10:
            return True
        return False


class Husband(Person):
    count_money = 0

    def pet_the_cat(self):
        super(Husband, self).pet_the_cat()

    def eating(self):
        super(Husband, self).eating()

    def playing(self):
        print(f'{self.name} играет за компьютером')
        self.degree_of_happiness += 20
        self.degree_of_satiety -= 10

    def working(self):
        print(f'{self.name} работает')
        self.count_money += 150
        self.house.money += 150
        self.degree_of_satiety -= 10


class Wife(Person):
    count_fur_coat = 0

    def pet_the_cat(self):
        super(Wife, self).pet_the_cat()

    def eating(self):
        super(Wife, self).eating()

    def shopping_for_food(self):
        print(f'{self.name} покупает еду')
        self.house.person_food += 10
        self.house.cat_food += 10
        self.house.money -= 20
        self.degree_of_satiety -= 10

    def buy_a_fur_coat(self):
        if self.house.money >= 350:
            self.count_fur_coat += 1
            print('Покупаем шубу')
            self.degree_of_happiness += 60
            self.house.money -= 350
        else:
            print('Денег на шубу нет')
        self.degree_of_satiety -= 10

    def cleaning(self):
        print(f'{self.name} убирается')
        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        self.degree_of_satiety -= 10


class Cat(FamilyMember):
    count_cat_food = 0

    def eating(self):
        if self.house.cat_food >= 10:
            self.count_cat_food += 10
            self.degree_of_satiety += 10 * 2
            self.house.cat_food -= 10
            print(f'{self.name} поел на 20 единиц еды')
        elif self.house.cat_food == 0:
            print(f'{self.name} не поел')
            print('Еда закончилась')
        else:
            self.count_cat_food += self.house.cat_food
            self.degree_of_satiety += self.house.cat_food * 2
            print(f'{self.name} опустошил весь запас корма в {self.house.cat_food} единиц, '
                  f'поел на {self.house.cat_food * 2} пункта')
            self.house.cat_food = 0

    def sleep(self):
        print('Кот спит')
        self.degree_of_satiety -= 10

    def tear_wallpaper(self):
        print('Кот дерет обои')
        self.house.dirt += 5
        self.degree_of_satiety -= 10


class House:
    def __init__(self):
        self.money = 100
        self.person_food = 50
        self.cat_food = 30
        self.dirt = 0

    def dirt_every_day(self):
        self.dirt += 5

    def is_dirty(self):
        if self.dirt >= 90:
            return True
        return False


our_house = House()

husband = Husband('Саня', our_house)
wife = Wife('Даша', our_house)
cat = Cat('Барсик', our_house)

family = [husband, wife, cat]

day = 0
while day != 365:
    day += 1
    print(f'День {day}')
    our_house.dirt_every_day()

    random_for_member = random.randint(0, len(family) - 1)

    if random_for_member == 0:
        random_for_move = random.randint(1, 4)
        if random_for_move == 1:
            husband.pet_the_cat()
        elif random_for_move == 2:
            husband.eating()
        elif random_for_move == 3:
            husband.playing()
        else:
            husband.working()
    elif random_for_member == 1:
        random_for_move = random.randint(1, 5)
        if random_for_move == 1:
            wife.pet_the_cat()
        elif random_for_move == 2:
            wife.eating()
        elif random_for_move == 3:
            wife.shopping_for_food()
        elif random_for_move == 4:
            wife.buy_a_fur_coat()
        else:
            wife.cleaning()
    else:
        random_for_move = random.randint(1, 3)
        if random_for_move == 1:
            cat.eating()
        elif random_for_move == 2:
            cat.sleep()
        else:
            cat.tear_wallpaper()

    husband.happiness_falls_every_day()
    wife.happiness_falls_every_day()

    count_dead = 0
    for i_member in family:
        if i_member.is_dead_of_hunger():
            print(f'{i_member.name} умер(-ла) от голода')
            count_dead += 1
    if count_dead > 0:
        break

    for i_member in range(0, 2):
        if family[i_member].is_dead_of_depression():
            print(f'{family[i_member].name} умер от депрессии')
            count_dead += 1
    if count_dead > 0:
        break

print()
print('В итоге:')
print(f'Было заработано денег - {husband.count_money}')
print(f'Съедено еды мужем и женой - {wife.count_food + husband.count_food}\nКотом - {cat.count_cat_food}')
print(f'Куплено шуб - {wife.count_fur_coat}')
