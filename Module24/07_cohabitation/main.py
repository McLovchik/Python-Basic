import random


class House:
    count_food = 50
    money = 0


class Human:
    degree_of_satiety = 50

    def __init__(self, name, house, earnings, food_eat, satiety_after_work_and_play):
        self.name = name
        self.house = house
        self.earnings = earnings
        self.food_eat = food_eat
        self.satiety_after_work_and_play = satiety_after_work_and_play

    def eating(self):
        self.degree_of_satiety += self.food_eat
        self.house.count_food -= self.food_eat

    def working(self):
        self.degree_of_satiety -= self.satiety_after_work_and_play
        self.house.money += self.earnings

    def playing(self):
        self.degree_of_satiety -= self.satiety_after_work_and_play

    def shopping_for_food(self):
        self.house.count_food += 10
        self.house.money -= 10

    def is_dead(self):
        if self.degree_of_satiety <= 0:
            return True
        return False


house_for_two = House()
man = Human('Саня', house_for_two, 4500, 150, 2)
woman = Human('Даша', house_for_two, 1500, 100, 2)
people = [man, woman]

day = 0
while day != 365:
    day += 1
    random_number = random.randint(1, 6)

    for i_person in people:
        if i_person.degree_of_satiety < 20 and i_person.house.count_food >= i_person.food_eat:
            i_person.eating()
        elif i_person.house.count_food < 10:
            if i_person.house.money >= 10:
                i_person.shopping_for_food()
        elif i_person.house.money < 50:
            i_person.working()
        elif random_number == 1:
            i_person.working()
        elif random_number == 2 and i_person.house.count_food >= i_person.food_eat:
            i_person.eating()
        else:
            i_person.playing()

    for i_person in people:
        if i_person.is_dead():
            print(i_person.name, 'is dead on', day, 'day')
            day = 365
            break
