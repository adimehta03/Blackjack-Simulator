from tkinter import *

from Game import Game

game = Game()


def start():
    label_winner["text"] = "Winner: "
    game.startGame()
    print_player_cards(label_cards, label_points, game.getPlayer())
    print_player_cards(label_dealer_cards, label_dealer_points, game.getDealer())
    button_start["state"] = DISABLED
    button_take_card.config(state='normal')
    button_stop.config(state='normal')


def print_player_cards(cards_labels, label_point, player):
    cards_labels["text"] = player.get_cards_text()
    label_point["text"] = player.get_player_point()


def disable_control_buttons():
    button_take_card["state"] = DISABLED
    button_stop["state"] = DISABLED


def take_card():
    """Give card to player. Prints cards in player hand"""
    game.give_card_to_player(game.getPlayer())
    print_player_cards(label_cards, label_points, game.getPlayer())

    """If player has Black Jack, dealer starts taking cards"""
    if game.getPlayer().get_player_point() == 21:
        disable_control_buttons()
        dealer_take_card()

    if game.getPlayer().get_player_point() > 21:
        label_winner["text"] = "Dealer Won"
        disable_control_buttons()
        button_start.config(state='normal')


def dealer_take_card():
    button_take_card["state"] = DISABLED
    button_stop["state"] = DISABLED
    game.give_card_to_player(game.getDealer())
    print_player_cards(label_dealer_cards, label_dealer_points, game.getDealer())
    if game.getDealer().get_player_point() > game.getPlayer().get_player_point():
        button_start.config(state='normal')
        if game.getDealer().get_player_point() <= 21:
            label_winner["text"] = "Dealer Won"
            return
        else:
            label_winner["text"] = "Player Won"
            return
    root.after(1000, dealer_take_card)


root = Tk()
root.title("BlackJack Simulator") 
button_start = Button(root, text="Start the game", command=start)
button_start.pack()
label_player = Label(root, text="Human").pack()
label_cards = Label(root, text="Cards")
label_cards.pack()
label_points = Label(root, text="Points")
label_points.pack()

frame = Frame(root)
button_take_card = Button(frame, text="Take a card", command=take_card, state=DISABLED)
button_take_card.pack(side='left')
button_stop = Button(frame, text="Stop", command=dealer_take_card, state=DISABLED)
button_stop.pack()
frame.pack()

label_dealer = Label(root, text="Dealer")
label_dealer.pack()
label_dealer_cards = Label(root, text="Cards")
label_dealer_cards.pack()
label_dealer_points = Label(root, text="Points")
label_dealer_points.pack()
label_winner = Label(root, text="The winner is: ")
label_winner.pack()

root.mainloop()
