def how_are_you(func):
    answer = input('Как дела? ')
    if answer:
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
