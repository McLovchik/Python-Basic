import random

karma_file = open('karma.log', 'w', encoding='utf-8')


class KillError(Exception):
    def __str__(self):
        return 'Умер'


class DrunkError(Exception):
    def __str__(self):
        return 'Напился'


class CarCrashError(Exception):
    def __str__(self):
        return 'Сбила машина'


class GluttonyError(Exception):
    def __str__(self):
        return 'Чревоугодствует'


class DepressionError(Exception):
    def __str__(self):
        return 'В депрессии'


exc_list = [KillError('Умер'), DrunkError('Напился'), CarCrashError('Сбила машина'),
            GluttonyError('Чревоугодствует'), DepressionError('В депрессии')]


def one_day():
    random_karma = random.randint(1, 7)
    random_for_call_exc = random.randint(1, 10)
    if random_for_call_exc == 1:
        random_for_exc = random.randint(0, 4)
        raise exc_list[random_for_exc]
    return random_karma


karma_points = 0
while karma_points < 500:
    try:
        karma_points += one_day()
    except KillError as exc_k_e:
        karma_file.write(f'{exc_k_e}\n')
    except DrunkError as exc_d_e:
        karma_file.write(f'{exc_d_e}\n')
    except CarCrashError as exc_c_c_e:
        karma_file.write(f'{exc_c_c_e}\n')
    except GluttonyError as exc_g_e:
        karma_file.write(f'{exc_g_e}\n')
    except DepressionError as exc_de_e:
        karma_file.write(f'{exc_de_e}\n')

karma_file.close()
