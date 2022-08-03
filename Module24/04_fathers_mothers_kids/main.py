class Parent:
    def __init__(self, parent_name, parent_age, child_list):
        self.parent_name = parent_name
        self.parent_age = parent_age
        self.child_list = child_list

    def __str__(self):
        return 'Имя родителя: ' + self.parent_name + '\n' + \
               'Возраст родителя: ' + str(self.parent_age) + '\n' + '\n' + \
               'Дети: ' + '\n' + '\n' + '\n'.join([str(i_child) for i_child in self.child_list])

    def soothe_the_child(self, child):
        print('Успокаиваем', child.child_name)
        for i_child in self.child_list:
            if i_child is child:
                if i_child.state_of_calm != 1:
                    i_child.state_of_calm += 1
                else:
                    print('Ребенок итак спокоен\n')
        print('Теперь состояние спокойствия ребенка -', child.child_name, '-',
              Child.states_of_calm[child.state_of_calm], '\n')

    def feed_the_baby(self, child):
        print('Кормим', child.child_name)
        for i_child in self.child_list:
            if i_child is child:
                if i_child.state_of_hunger != 2:
                    i_child.state_of_hunger += 1
                else:
                    print('Ребенок итак сыт\n')
        print('Теперь состояние голода ребенка -', child.child_name, '-',
              Child.states_of_hunger[child.state_of_hunger], '\n')


class Child:
    states_of_calm = {0: 'Буйный', 1: 'Спокойный'}
    states_of_hunger = {0: 'Голодный', 1: 'Можно немного поесть', 2: 'Сытый'}

    def __init__(self, child_name, child_age, state_of_calm=1, state_of_hunger=2):
        self.child_name = child_name
        self.child_age = child_age
        self.state_of_calm = state_of_calm
        self.state_of_hunger = state_of_hunger

    def __str__(self):
        return 'Имя ребенка: {}\nВозраст ребенка: {}\n{}\n{}\n'.format(
                self.child_name,
                self.child_age,
                Child.states_of_calm[self.state_of_calm],
                Child.states_of_hunger[self.state_of_hunger]
            )


misha = Child('Мишка', 4, 0, 0)
sasha = Child('Сашка', 4, 0, 0)
parent_1 = Parent('Саня', 21, [misha, sasha])
print(parent_1.__str__())
parent_1.soothe_the_child(misha)
parent_1.feed_the_baby(sasha)
