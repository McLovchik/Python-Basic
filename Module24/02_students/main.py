class Student:
    def __init__(self, full_name, group, academic_performance):
        self.full_name = full_name
        self.group = group
        self.academic_performance = academic_performance

    def average_score(self):
        return sum(self.academic_performance) / len(self.academic_performance)

    def __str__(self):
        result = f'{self.full_name} {self.group} {self.academic_performance}'
        return result


students = [
    Student('Петров Иван', 1, [1, 2, 3, 4, 5]),
    Student('Петров Иван', 2, [2, 2, 3, 4, 5]),
    Student('Петров Иван', 3, [1, 5, 3, 4, 5]),
    Student('Петров Иван', 4, [5, 5, 3, 5, 5]),
    Student('Петров Иван', 5, [4, 2, 1, 4, 5]),
    Student('Петров Иван', 6, [5, 2, 3, 3, 5]),
    Student('Петров Иван', 7, [1, 4, 1, 4, 5]),
    Student('Петров Иван', 8, [5, 2, 2, 4, 5]),
    Student('Петров Иван', 9, [4, 2, 2, 1, 5]),
    Student('Петров Иван', 10, [2, 2, 3, 1, 1]),
]

students_sorted_by_average_score = sorted(students, key=lambda student: student.average_score())
print(*students_sorted_by_average_score, sep='\n')
