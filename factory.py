from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def game_factory(config: dict) -> CardGame:
    cli = CLI()
    player_names: list[str] = config["names"]
    players: tuple[Player] = Player.from_names(player_names)
    scoreboard = ScoreBoard.from_names(player_names)
    game_pile = Pile.from_seed(seed=config["seed"], name="game")
    discard_pile = Pile(name="discard")
    return CardGame(
        players=players,
        game_pile=game_pile,
        discard_pile=discard_pile,
        ui=cli,
        scoreboard=scoreboard,
    )
