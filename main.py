from card import Pile
from game import CardGame
from player import Player
from ui import CLI


def main():
    evan = Player(name="Evan")
    viola = Player(name="Viola")
    pile = Pile.from_str(pile_str="AKKQQQ", name="game pile")
    removed_pile = Pile(name="removed cards pile")
    cli = CLI()
    nb_rounds = 3
    cli.render_pile(pile=pile, separator=True)
    game = CardGame(player=viola, other_player=evan, pile=pile, removed_cards_pile=removed_pile, ui=cli)

    game.run(nb_rounds=nb_rounds)


if __name__ == "__main__":
    main()
