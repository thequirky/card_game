from card import Pile
from game import CardGame
from player import Player
from ui import CLI


def main():
    evan = Player(name="Evan")
    viola = Player(name="Viola")
    pile = Pile.from_str(seed_str="AKKQQQQ", name="game")
    removed_pile = Pile(name="discard")
    cli = CLI()
    nb_rounds = 5
    game = CardGame(player=viola, other_player=evan, pile=pile, removed_cards_pile=removed_pile, ui=cli)
    game.run(nb_rounds=nb_rounds)


if __name__ == "__main__":
    main()
