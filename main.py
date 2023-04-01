from deck import Deck
from game import CardGame
from player import Player
from ui import CLI


def main():
    evan = Player(name="Evan")
    viola = Player(name="Viola")
    deck = Deck.from_str(card_string="aaakkkqqq", shuffle=True)
    cli = CLI()
    nb_rounds = 3
    cli.show_cards_pile(deck=deck, separator=True)
    game = CardGame(player=viola, other_player=evan, deck=deck, ui=cli)
    game.run(nb_rounds=nb_rounds)


if __name__ == "__main__":
    main()
