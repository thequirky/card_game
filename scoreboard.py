from __future__ import annotations

import logging
from dataclasses import dataclass, field


@dataclass
class ScoreBoard:
    rounds_won: dict[str, int] = field(default_factory=dict)  # {name: rounds_won}
    scores: dict[str, int] = field(default_factory=dict)  # {name: score}

    @property
    def player_names(self) -> tuple[str]:
        return tuple(self.scores.keys())

    @classmethod
    def from_names(cls, names: list[str]) -> ScoreBoard:
        board = cls()
        names = [name.strip().capitalize() for name in names]
        unique_names = list(set(names))
        if unique_names != names:
            logging.warning("There are duplicate names.")
        for name in unique_names:
            board.scores[name] = 0
            board.rounds_won[name] = 0
            logging.info(f"{name} was added to the scoreboard.")
        return board

    def is_registered(self, name: str) -> bool:
        return name in self.player_names

    def register(self, name: str) -> None:
        if self.is_registered(name):
            logging.warning(f"{name} is already on the scoreboard.")
            return
        self.scores[name] = 0
        self.rounds_won[name] = 0
        logging.info(f"{name} was added to the scoreboard.")

    def get_score_of(self, name: str) -> int | None:
        if not self.is_registered(name):
            logging.error(f"{name} not registered -> could not get score.")
            return
        return self.scores[name]

    def increase_player_score_by(self, name: str, value: int) -> None:
        if not self.is_registered(name):
            logging.error(f"{name} not registered -> could not increase score.")
            return
        self.scores[name] += value

    def increment_player_rounds_won(self, name: str) -> None:
        if not self.is_registered(name):
            logging.error(f"{name} not registered -> could not increment rounds won.")
            return
        self.rounds_won[name] += 1

    def reset_scores(self) -> None:
        self.scores = {k: 0 for k in self.scores}

    def reset_rounds(self) -> None:
        self.rounds_won = {k: 0 for k in self.rounds_won}

    # todo: add string representation
    # def __str__(self) -> str:
    #     return


if __name__ == "__main__":
    from player import Player

    logging.basicConfig(level=logging.INFO)

    names = ["evan", "viola", "viola"]
    p1, p2, p3 = Player.from_names(names)
    scoreboard = ScoreBoard.from_names(names)
    # scoreboard.register(p1.name)
    print(scoreboard)
    scoreboard.increase_player_score_by(name=p2.name, value=100)
    print(scoreboard)
    scoreboard.increase_player_score_by(name="lenka", value=50)
    scoreboard.increment_player_rounds_won(p2.name)
    print(scoreboard)
    scoreboard.reset_scores()
    print(scoreboard)
