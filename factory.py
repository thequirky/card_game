import logging

from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def deduplicate(names: tuple[str]) -> tuple[str]:
    for name in names:
        if not isinstance(name, str):
            raise ValueError(f"{name} is not a string.")
    unique_names = {n.strip().capitalize() for n in names}
    if len(unique_names) != len(names):
        logging.warning("Duplicate names found.")
    return tuple(unique_names)


def game_factory(config: dict) -> CardGame:
    ui = CLI()
    player_names = deduplicate(config["names"])
    players = Player.from_names(player_names)
    scoreboard = ScoreBoard.from_players(players)
    game_pile = Pile.from_seed(seed=config["seed"], name="game")
    return CardGame(
        players=players,
        game_pile=game_pile,
        ui=ui,
        scoreboard=scoreboard,
    )
