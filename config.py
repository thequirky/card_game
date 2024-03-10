from dataclasses import dataclass

from card.pile import Pile
from game import CardGame
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


@dataclass
class Config:
    names: list[str]
    seed: str
    nb_rounds: int = 0
    game_pile_name: str = "game"
    ui = CLI()

    @property
    def players(self) -> list[Player]:
        return Player.from_names(self.names)

    @property
    def scoreboard(self) -> ScoreBoard:
        return ScoreBoard.from_players(self.players)

    @property
    def game_pile(self) -> Pile:
        return Pile.from_seed(seed=self.seed, name=self.game_pile_name)

    @property
    def game(self) -> CardGame:
        return CardGame(
            players=self.players,
            game_pile=self.game_pile,
            ui=self.ui,
            scoreboard=self.scoreboard,
        )

    def run(self) -> None:
        self.game.run(self.nb_rounds)
