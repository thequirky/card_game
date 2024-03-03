from __future__ import annotations

import logging


class ScoreBoard:
    def __init__(self, names: list[str]) -> None:
        self.names = self.get_unique_names(names)
        logging.info(f"{self.names} added to the scoreboard.")
        self.scores: dict[str, int] = {n: 0 for n in self.names}
        self.rounds_won: dict[str, int] = {n: 0 for n in self.names}

    def is_registered(self, name: str) -> bool:
        return name in self.names

    def increment_score(self, name: str, value: int) -> None:
        if not self.is_registered(name):
            raise ValueError(f"{name} not registered -> could not increase score.")
        self.scores[name] += value

    def increment_rounds(self, name: str) -> None:
        if not self.is_registered(name):
            raise ValueError(f"{name} not registered -> could not increment rounds won.")
        self.rounds_won[name] += 1

    @property
    def score_leaders_to_rounds(self) -> dict[str, int]:
        highest_score = max(self.scores.values())
        return {n: self.rounds_won[n] for n, s in self.scores.items() if s == highest_score}

    def get_game_winners(self) -> list[str]:
        if len(self.score_leaders_to_rounds) > 1:
            return self.resolve_tie_with_rounds()
        return self.score_leaders_to_rounds.keys()

    @property
    def winners(self) -> list[str]:
        highest_nb_rounds = max(self.score_leaders_to_rounds.values())
        return [n for n, r in self.score_leaders_to_rounds.items() if r == highest_nb_rounds]

    def is_unresolvable_tie(self) -> bool:
        return len(self.names) == 2 and len(self.winners) > 1

    def resolve_tie_with_rounds(self) -> list[str]:
        if self.is_unresolvable_tie():
            return []
        return self.winners

    @staticmethod
    def get_unique_names(names: list[str]) -> list[str]:
        unique_names = {name.strip().capitalize() for name in names}
        if len(unique_names) < len(names):
            raise ValueError("There are duplicate names.")
        return list(unique_names)

    @classmethod
    def from_players(cls, players: list[Player]) -> ScoreBoard:
        return cls(names=[p.name for p in players])

    def __repr__(self) -> str:
        return f"ScoreBoard(names={self.names}, scores={self.scores}, rounds_won={self.rounds_won})"

    def __str__(self) -> str:
        return f"scores={self.scores}, rounds_won={self.rounds_won}"


if __name__ == "__main__":
    from player import Player

    logging.basicConfig(level=logging.INFO)

    names = ("evan", "viola", "lenka")
    players = Player.from_names(names)
    scoreboard = ScoreBoard.from_players(players)
    scoreboard.actions.increment_score(players[1].name, value=100)
    print(scoreboard)
    scoreboard.actions.increment_score(players[1].name, value=50)
    print(scoreboard)
    scoreboard.actions.increment_rounds(players[1].name)
    print(scoreboard)
