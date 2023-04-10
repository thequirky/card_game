from card import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


class GameConfig:
    def __init__(self, names: list[str], pile_str: str) -> None:
        self.cli = CLI()
        self.player1 = Player(names[0])
        self.player2 = Player(names[1])
        self.scoreboard = ScoreBoard()
        self.scoreboard.register(names[0])
        self.scoreboard.register(names[1])
        self.game_pile = Pile.from_str(seed_str=pile_str, name="game")
        self.discard_pile = Pile("discard")
        self.ui = CLI()
        self.game = CardGame(
            player=self.player1,
            other_player=self.player2,
            game_pile=self.game_pile,
            discard_pile=self.discard_pile,
            ui=self.ui,
            scoreboard=self.scoreboard,
        )