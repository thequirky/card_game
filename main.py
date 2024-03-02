import logging

from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI

NB_ROUNDS = 0
# NB_ROUNDS = 10

# CONFIG = {"names": ("evan", "viola"), "seed": "AKKQQQJJJJ"}
# CONFIG = {"names": ("evan", "viola", "lenka"), "seed": "AAKKKQQQQJJJJ"}
CONFIG = {"names": ("evan", "viola", "olivia", "lenka"), "seed": "AAAAKKKKQQQQJJJJ"}


def game_factory(config: dict) -> CardGame:
    ui = CLI()
    player_names = config["names"]
    players = Player.from_names(player_names)
    scoreboard = ScoreBoard.from_players(players)
    game_pile = Pile.from_seed(seed=config["seed"], name="game")
    return CardGame(
        players=players,
        game_pile=game_pile,
        ui=ui,
        scoreboard=scoreboard,
    )


def main():
    logging.basicConfig(level=logging.INFO)

    game = game_factory(CONFIG)
    game.run(NB_ROUNDS)


if __name__ == "__main__":
    main()
