from Deck import Deck
from Player import Player


class Game:
    def startGame(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        """Give one card to dealer and player"""
        self.player.take_card(self.deck.give_card())
        self.dealer.take_card(self.deck.give_card())

    def give_card_to_player(self, player):
        player.take_card(self.deck.give_card())

    def getPlayer(self):
        return self.player

    def getDealer(self):
        return self.dealer