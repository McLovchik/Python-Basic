class Fire:
    title = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()


class Air:
    title = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Water:
    title = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Earth:
    title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()


class Storm:
    title = 'Шторм'


class Steam:
    title = 'Пар'


class Dirt:
    title = 'Грязь'


class Lightning:
    title = 'Молния'


class Dust:
    title = 'Пыль'


class Lava:
    title = 'Лава'


first_elem = Water()
second_elem = Air()
result = first_elem + second_elem

if result:
    print(f"Смешиваем '{first_elem.title}' c '{second_elem.title}' и получаем '{result.title}'")
else:
    print('None')
