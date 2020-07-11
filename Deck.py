from Card import Card
from random import randint


class Deck:
    def __init__(self):
        """Fill the deck"""
        self.list = []
        for suit in Card.suit_names:
            for value in range(2, 11):
                card = Card(suit, value)
                self.list.append(card)
            for value in range(0, 4):
                card = Card(suit, Card.cards_with_image[value])
                self.list.append(card)

    def get_deck(self):
        """Return deck"""
        return self.list

    def give_card(self):
        """Return random card from deck and remove it from deck"""
        card = self.list[randint(0, len(self.list) - 1)]
        self.list.remove(card)
        return card


