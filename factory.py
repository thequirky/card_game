from card import Pile
from game import CardGame, CardActions, ScoringActions
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def game_factory(config: dict) -> CardGame:
    ui = CLI()
    player_names = config["names"]
    players = Player.from_names(player_names)
    scoreboard = ScoreBoard(player_names)
    game_pile = Pile.from_seed(seed=config["seed"], name="game")
    discard_pile = Pile(name="discard")
    scoring_actions = ScoringActions(players=players, scoreboard=scoreboard)
    card_actions = CardActions(players=players, game_pile=game_pile, discard_pile=discard_pile)
    return CardGame(
        players=players,
        game_pile=game_pile,
        discard_pile=discard_pile,
        ui=ui,
        scoreboard=scoreboard,
        scoring_actions=scoring_actions,
        card_actions=card_actions,
    )
