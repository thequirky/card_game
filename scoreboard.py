from __future__ import annotations

import logging


class ScoreBoard:
    def __init__(self, names: list[str]) -> None:
        unique_names = self.get_unique(names)
        self.names = unique_names
        self.scores: dict[str, int] = {n: 0 for n in unique_names}
        self.rounds_won: dict[str, int] = {n: 0 for n in unique_names}
        logging.info(f"{self.names} added to the scoreboard.")

    def get_unique(self, names: list[str]) -> set[str]:
        unique_names = {name.strip().capitalize() for name in names}
        if len(names) != len(unique_names):
            logging.warning("There are duplicate names.")
        return unique_names

    def is_registered(self, name: str) -> bool:
        return name in self.names

    def register(self, name: str) -> None:
        if self.is_registered(name):
            logging.warning(f"{name} is already on the scoreboard.")
            return
        self.scores[name] = 0
        self.rounds_won[name] = 0
        logging.info(f"{name} added to the scoreboard.")

    def get_score_of(self, name: str) -> int | None:
        if not self.is_registered(name):
            logging.error(f"{name} not registered -> could not get score.")
            return
        return self.scores[name]

    def increment_score(self, name: str, value: int) -> None:
        if not self.is_registered(name):
            logging.error(f"{name} not registered -> could not increase score.")
            return
        self.scores[name] += value

    def increment_rounds_won(self, name: str) -> None:
        if not self.is_registered(name):
            logging.error(f"{name} not registered -> could not increment rounds won.")
            return
        self.rounds_won[name] += 1

    def reset_scores(self) -> None:
        self.scores = {k: 0 for k in self.scores}

    def reset_rounds(self) -> None:
        self.rounds_won = {k: 0 for k in self.rounds_won}

    # todo: add nicer string representation
    def __str__(self) -> str:
        return f"Scores: {str(self.scores)}, Rounds won: {str(self.rounds_won)}"


if __name__ == "__main__":
    from player import Player

    logging.basicConfig(level=logging.INFO)

    names = ["evan", "viola", "viola"]
    p1, p2, p3 = Player.from_names(names)
    scoreboard = ScoreBoard(names)
    scoreboard.register(p1.name)
    print(scoreboard)
    scoreboard.increment_score(name=p2.name, value=100)
    print(scoreboard)
    scoreboard.increment_score(name="lenka", value=50)
    scoreboard.increment_rounds_won(p2.name)
    print(scoreboard)
    scoreboard.reset_scores()
    print(scoreboard)
