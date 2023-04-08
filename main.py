from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def main():
    evan = Player(name="Evan")
    viola = Player(name="Viola")
    scoreboard = ScoreBoard()
    scoreboard.register_player(evan.name)
    scoreboard.register_player(viola.name)
    pile = Pile.from_str(seed_str="AKKQQQQ", name="game")
    discard_pile = Pile(name="discard")
    nb_rounds = 5
    cli = CLI()
    game = CardGame(player=viola,
                    other_player=evan,
                    pile=pile,
                    discard_pile=discard_pile,
                    ui=cli,
                    scoreboard=scoreboard)

    game.run(nb_rounds=nb_rounds)


if __name__ == "__main__":
    main()
