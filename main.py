from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def main():
    # settings:
    cli = CLI()
    player1 = Player("evan")
    player2 = Player("viola")
    names = [player1.name, player2.name]
    scoreboard = ScoreBoard.from_names(names)
    pile = Pile.from_str(seed_str="AKKQQQJJJJ", name="game")
    discard_pile = Pile("discard")
    nb_rounds = 5

    game = CardGame(
        player=player1,
        other_player=player2,
        pile=pile,
        discard_pile=discard_pile,
        ui=cli,
        scoreboard=scoreboard,
    )

    game.run(nb_rounds)


if __name__ == "__main__":
    main()
