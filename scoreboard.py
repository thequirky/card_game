from __future__ import annotations

import logging


class Actions:
    def __init__(self, names: tuple[str], scores: dict[str, int], rounds_won: dict[str, int]) -> None:
        self.names = names
        self.scores = scores
        self.rounds_won = rounds_won

    def is_registered(self, name: str) -> bool:
        return name in self.names

    def increment_score_of(self, name: str, value: int) -> None:
        if not self.is_registered(name):
            raise ValueError(f"{name} not registered -> could not increase score.")
        self.scores[name] += value

    def increment_rounds_of(self, name: str) -> None:
        if not self.is_registered(name):
            raise ValueError(f"{name} not registered -> could not increment rounds won.")
        self.rounds_won[name] += 1

    def get_game_winners(self) -> tuple[str]:
        highest_score = max(self.scores.values())
        score_leaders_to_rounds = {n: self.rounds_won[n] for n, s in self.scores.items() if s == highest_score}
        if len(score_leaders_to_rounds) > 1:
            return self.resolve_tie_with_rounds(score_leaders_to_rounds)
        return tuple(score_leaders_to_rounds.keys())

    def resolve_tie_with_rounds(self, score_leaders_to_rounds: dict[str, int]) -> tuple[str]:
        highest_nb_rounds = max(score_leaders_to_rounds.values())
        winners = tuple(n for n, r in score_leaders_to_rounds.items() if r == highest_nb_rounds)
        unresolvable_tie = len(self.names) == 2 and len(winners) > 1
        if unresolvable_tie:
            return tuple()
        return winners


class ScoreBoard:
    def __init__(self, names: tuple[str]) -> None:
        self._names = names
        self._scores = {n: 0 for n in names}
        self._rounds_won = {n: 0 for n in names}
        logging.info(f"{self.names} added to the scoreboard.")
        self.actions = Actions(names=self.names, scores=self.scores, rounds_won=self.rounds_won)

    @property
    def names(self) -> tuple[str]:
        return self._names

    @property
    def scores(self) -> dict[str, int]:
        return self._scores

    @property
    def rounds_won(self) -> dict[str, int]:
        return self._rounds_won

    @classmethod
    def from_players(cls, players: tuple[Player]) -> ScoreBoard:
        names = tuple(p.name for p in players)
        return cls(names)

    def register(self, name: str) -> None:
        if self.actions.is_registered(name):
            raise ValueError(f"{name} is already on the scoreboard.")
        self.scores[name] = 0
        self.rounds_won[name] = 0
        logging.info(f"{name} added to the scoreboard.")

    def __repr__(self) -> str:
        return f"ScoreBoard(names={self.names}, scores={self.scores}, rounds_won={self.rounds_won})"

    def __str__(self) -> str:
        return f"scores={self.scores}, rounds_won={self.rounds_won}"


if __name__ == "__main__":
    from factory import deduplicate
    from player import Player

    logging.basicConfig(level=logging.INFO)

    names = ("evan", "viola", "lenka")
    names = deduplicate(names)
    players = Player.from_names(names)
    scoreboard = ScoreBoard.from_players(players)
    scoreboard.actions.increment_score_of(players[1].name, value=100)
    print(scoreboard)
    scoreboard.actions.increment_score_of(players[1].name, value=50)
    print(scoreboard)
    scoreboard.actions.increment_rounds_of(players[1].name)
    print(scoreboard)
