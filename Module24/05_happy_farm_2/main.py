class Potato:
    states = {0: 'Отсутсвует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        # for i_potato in self.potatoes:
        #     if not i_potato.is_ripe():
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            # break
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True


class Gardener:

    def __init__(self, gardener_name, garden):
        self.gardener_name = gardener_name
        self.garden = garden

    def take_care_of_the_garden(self):
        self.garden.are_all_ripe()
        for _ in range(3):
            self.garden.grow_all()
            self.garden.are_all_ripe()
            self.harvest()

    def harvest(self):
        if self.garden.are_all_ripe():
            print('Собираем урожай')
            self.garden.potatoes = []
            print('Картошки больше нет')


gardener_misha = Gardener('Миша', PotatoGarden(5))
gardener_misha.take_care_of_the_garden()