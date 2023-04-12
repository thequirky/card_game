from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def game_factory(config: dict) -> CardGame:
    cli = CLI()
    player_names = config["names"]
    players = [Player(name) for name in player_names]
    scoreboard = ScoreBoard()
    for player in players:
        scoreboard.register(player.name)
    game_pile = Pile.from_seed(seed=config["seed"], name="game")
    discard_pile = Pile("discard")
    return CardGame(
        player=players[0],
        other_player=players[1],
        game_pile=game_pile,
        discard_pile=discard_pile,
        ui=cli,
        scoreboard=scoreboard,
    )
