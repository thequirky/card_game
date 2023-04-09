from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def main():
    p1 = Player("evan")
    p2 = Player("viola")
    scoreboard = ScoreBoard()
    scoreboard.register_player(p1.name)
    scoreboard.register_player(p2.name)
    pile = Pile.from_str(seed_str="AKKQQQJJJJ", name="game")
    discard_pile = Pile("discard")
    nb_rounds = 3
    cli = CLI()
    game = CardGame(
        player=p1,
        other_player=p2,
        pile=pile,
        discard_pile=discard_pile,
        ui=cli,
        scoreboard=scoreboard,
    )

    game.run(nb_rounds)


if __name__ == "__main__":
    main()
