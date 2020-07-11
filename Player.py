from Deck import Deck


class Player:
    def __init__(self):
        self.hand = []
        self.deck = Deck()
        self.point = 0

    def take_card(self, card):
        """Give card in player hand, increace player points"""
        self.hand.append(card)
        self.point += card.get_card_value()

    def get_player_point(self):
        """return player points"""
        return self.point

    def get_cards_text(self):
        """return string card values and name"""
        cards_value = ""
        for card in self.hand:
            cards_value += " " + str(card.get_card_image_val()) + " " + card.get_card_suit()
        return cards_value
