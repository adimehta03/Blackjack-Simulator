class Card:
    suit_names = ("hearts", "spades", "clubs", "diamonds")
    cards_with_image = ("Jack", "Queen", "King", "Ace")

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_card_value(self):
        """Return value - 10 for cards with image"""
        if self.value == "Ace":
            return 11
        if self.value in self.cards_with_image:
            return 10
        else:
            return self.value

    def get_card_image_val(self):
        """Return text value of the card"""
        return self.value

    def get_card_suit(self):
        """Return card type """
        return self.suit

