# Напишите программу, которая реализует игру «Крестики-нолики».

class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - строка
    #   - столбец
    #   - номер

    def __init__(self, is_busy, value):
        self.is_busy = is_busy
        self.value = value


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки

    def __init__(self, length):
        self.length = length

    cell_list = []

    def create_board(self):
        for i_line in range(1, self.length + 1):
            for i_col in range(1, self.length + 1):
                self.cell_list.append(Cell(False, '-'))
        return self.cell_list


def field_drawing(size, fun_list):
    fun_count = -1
    for _ in range(1, size + 1):
        for _ in range(1, size + 1):
            fun_count += 1
            print(fun_list[fun_count].value, end='  ')
        print(end='\n')


def is_end(fun_is_end_list):
    increase_for_diagonal_from_left_up = field_size + 1
    increase_for_diagonal_from_right_up = field_size - 1

    # горизонталь
    fun_is_end_count = 0
    for h_line in range(1, field_size + 1):
        if fun_is_end_list[fun_is_end_count].value != '-':
            fun_value = fun_is_end_list[fun_is_end_count].value
            count_filled_line = 1
            for h_col in range(2, field_size + 1):
                fun_is_end_count += 1
                if fun_value == fun_is_end_list[fun_is_end_count].value:
                    count_filled_line += 1
                else:
                    fun_is_end_count += 1
                    break
            if count_filled_line == field_size:
                return fun_value
        else:
            fun_is_end_count += 1

    # вертикаль
    for h_col in range(1, field_size + 1):
        count_filled_line = 0
        if fun_is_end_list[h_col - 1].value == 'x' or fun_is_end_list[h_col - 1].value == 'o':
            fun_value = fun_is_end_list[h_col - 1].value
            for h_line in range(h_col + field_size, field_size**2 - (field_size - h_col) + 1, field_size):
                if fun_value == fun_is_end_list[h_line - 1].value:
                    count_filled_line += 1
                else:
                    break
            if count_filled_line == field_size - 1:
                return fun_value

    # диагональ сверху слева в право низ
    count_filled_line = 0
    fun_value = fun_is_end_list[0].value
    if fun_value != '-':
        for i_diagonal in range(1 + increase_for_diagonal_from_left_up,
                                field_size ** 2 + 1, increase_for_diagonal_from_left_up):
            if fun_value == fun_is_end_list[i_diagonal - 1].value:
                count_filled_line += 1
            else:
                break
        if count_filled_line == field_size - 1:
            return fun_value

    # диагональ справа сверху в лево низ
    count_filled_line = 0
    fun_value = fun_is_end_list[field_size - 1].value
    if fun_value != '-':
        for i_diagonal in range(field_size + increase_for_diagonal_from_right_up,
                                field_size**2 - increase_for_diagonal_from_right_up + 1,
                                increase_for_diagonal_from_right_up):
            if fun_value == fun_is_end_list[i_diagonal - 1].value:
                count_filled_line += 1
            else:
                break
        if count_filled_line == field_size - 1:
            return fun_value


field_size = int(input('Введите размер поля: '))

board = Board(field_size)
my_cell_list = board.create_board()

# Вывод поля
print('Начальное поле')
field_drawing(field_size, my_cell_list)
print('Первые ходят крестики')

move_count = 0
is_there_a_winner = False
while move_count != field_size ** 2:
    print()
    move_count += 1
    if move_count % 2 != 0:
        x_or_o = 'x'
    else:
        x_or_o = 'o'
    while True:
        place = int(input(f'Введите номер поля, куда хотите поставить {x_or_o}: '))
        if not my_cell_list[place - 1].is_busy:
            my_cell_list[place - 1].value = x_or_o
            my_cell_list[place - 1].is_busy = True
            break
        else:
            print('Занято. Введите еще раз')
    print('Текущее поле')
    field_drawing(field_size, my_cell_list)
    if move_count >= field_size * 2 - 1:
        is_end_value = is_end(my_cell_list)
        if is_end_value:
            print(f'Выйграли {is_end_value}')
            is_there_a_winner = True
            break

if not is_there_a_winner:
    print('Ничья')
