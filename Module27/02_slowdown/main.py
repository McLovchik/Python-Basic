import time


def waiting(func):
    time.sleep(4)
    func()


@waiting
def get_data():
    print('Здесь что-то происходит...')
