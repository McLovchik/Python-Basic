import random


class Card:
    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck:
    #  Колода создаёт у себя объекты карт
    suits = ['Буби', 'Черви', 'Крести', 'Пики']
    cards_and_rank = {'Двойка': 2, 'Тройка': 3, 'Четверка': 4, 'Пятерка': 5,
                      'Шестёрка': 6, 'Семёрка': 7, 'Восьмёрка': 8, 'Девятка': 9,
                      'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': [11, 1]}

    def creating_card_objects(self):
        random_num_for_suits = random.randint(0, 3)
        random_num_for_cards = random.randint(0, 12)
        new_card = Card(self.suits[random_num_for_suits],
                        self.cards_and_rank[list(self.cards_and_rank)[random_num_for_cards]])
        return new_card.rank, self.suits[random_num_for_suits], list(self.cards_and_rank)[random_num_for_cards]
        # значение, масть и карта


class Player:
    #  Игрок, у которого есть имя и какие-то карты на руках
    def __init__(self, player_name, player_cards, player_points):
        self.player_name = player_name
        self.player_cards = player_cards
        self.player_points = player_points

    def print_cards(self):
        print(f'У вас на руках {self.player_cards}, что в сумме даёт {self.player_points} очков')


def create_card():
    player_deck = Deck()
    player_points = player_deck.creating_card_objects()
    if type(player_points[0]) is list:
        player_points = player_points[0][0], player_points[1], player_points[2]
    return player_points


# Начальная раздача карт игроку и дилеру
first_create_card_for_player = create_card()
second_create_card_for_player = create_card()

player = Player('Игрок', [(first_create_card_for_player[2], first_create_card_for_player[1]),
                (second_create_card_for_player[2], second_create_card_for_player[1])],
                first_create_card_for_player[0] + second_create_card_for_player[0])


first_create_card_for_dealer = create_card()
second_create_card_for_dealer = create_card()

dealer = Player('Дилер', [(first_create_card_for_dealer[2], first_create_card_for_dealer[1]),
                (second_create_card_for_dealer[2], second_create_card_for_dealer[1])],
                first_create_card_for_dealer[0] + second_create_card_for_dealer[0])


player.print_cards()
while True:
    if player.player_points > 21:
        print('Вы сгорели')
        break
    question = input('Хотите взять еще одну карту? ').lower()
    if question == 'да':
        new_create_card_for_player = create_card()
        player.player_cards.append((new_create_card_for_player[2], new_create_card_for_player[1]))
        player.player_points += new_create_card_for_player[0]
        player.print_cards()
    else:
        if player.player_points > dealer.player_points:
            print('Вы выйграли')
        elif player.player_points == dealer.player_points:
            print('Ничья')
        else:
            print('Вы проиграли')
        break
