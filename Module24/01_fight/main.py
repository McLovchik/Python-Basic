import random


class Unit:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        if type(self) == type(target):
            target.health -= 20
        else:
            raise TypeError


warriors = [Unit('First_Unit'), Unit('Second_Unit')]

while True:
    random_value = random.randint(0, 1)
    attacker, victim = warriors[random_value], warriors[random_value - 1]
    attacker.hit(victim)
    print(attacker.name, 'атаковал', victim.name)
    print('У', victim.name, 'осталось здоровья', victim.health, '\n')
    if victim.health == 0:
        print(attacker.name, 'победил!')
        break
