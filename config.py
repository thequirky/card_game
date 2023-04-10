from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


def config_game(name1: str, name2: str, pile_str: str) -> CardGame:
        cli = CLI()
        player1 = Player(name1)
        player2 = Player(name2)
        scoreboard = ScoreBoard()
        scoreboard.register(name1)
        scoreboard.register(name2)
        game_pile = Pile.from_str(seed_str=pile_str, name="game")
        discard_pile = Pile("discard")
        return CardGame(
            player=player1,
            other_player=player2,
            game_pile=game_pile,
            discard_pile=discard_pile,
            ui=cli,
            scoreboard=scoreboard,
        )
