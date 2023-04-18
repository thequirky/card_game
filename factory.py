from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def game_factory(config: dict) -> CardGame:
    ui = CLI()
    player_names = config["names"]
    players = Player.from_names(player_names)
    scoreboard = ScoreBoard.from_players(players)
    game_pile = Pile.from_seed(seed=config["seed"], name="game")
    discard_pile = Pile(name="discard")
    return CardGame(
        players=players,
        game_pile=game_pile,
        discard_pile=discard_pile,
        ui=ui,
        scoreboard=scoreboard,
    )
