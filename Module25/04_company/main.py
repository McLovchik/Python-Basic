class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return 'Имя: {name}, Фамилия: {surname}, Возраст: {age}'.format(
            name=self.__name,
            surname=self.__surname,
            age=self.__age
        )


class Employee(Person):
    def payroll_preparation(self):
        pass

    def __str__(self):
        info = super().__str__()
        info = ' '.join(
            (
                info,
                'Зарплата: {salary}'.format(salary=self.payroll_preparation())
            )
        )
        return info


class Manager(Employee):
    def payroll_preparation(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, volume_of_sales):
        super().__init__(name, surname, age)
        self.volume_of_sales = volume_of_sales

    def payroll_preparation(self):
        return 5000 + 0.05 * self.volume_of_sales


class Worker(Employee):
    def __init__(self, name, surname, age, hours_worked):
        super().__init__(name, surname, age)
        self.hours_worked = hours_worked

    def payroll_preparation(self):
        return 100 * self.hours_worked


list_workers = [
    Manager('Саня', 'Петров', 24),
    Manager('Даня', 'Нетров', 26),
    Manager('Ваня', 'Ретров', 34),
    Agent('Таня', 'Петрова', 24, 10000),
    Agent('Маша', 'Лысова', 21, 20000),
    Agent('Катя', 'Лышова', 27, 100000),
    Worker('Миша', 'Быстров', 30, 800),
    Worker('Дима', 'Качков', 35, 400),
    Worker('Петя', 'Сверчков', 20, 600)
]

for i_worker in list_workers:
    print(i_worker.__str__())
