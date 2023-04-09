from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def main():
    cli = CLI()
    p1 = Player("evan")
    p2 = Player("viola")
    names = [p1.name, p2.name]
    scoreboard = ScoreBoard.from_player_names(names=names, ui=cli)
    pile = Pile.from_str(seed_str="AKKQQQJJJJ", name="game")
    discard_pile = Pile("discard")
    nb_rounds = 5
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
