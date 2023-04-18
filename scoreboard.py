from __future__ import annotations

import logging


class ScoreBoard:
    def __init__(self, names: iter[str]) -> None:
        unique_names = self.get_unique_names(names)
        self._names = tuple(unique_names)
        self._scores: dict[str, int] = {n: 0 for n in unique_names}
        self._rounds_won: dict[str, int] = {n: 0 for n in unique_names}
        self._games_won: dict[str, int] = {n: 0 for n in unique_names}
        logging.info(f"{self.names} added to the scoreboard.")

    @staticmethod
    def get_unique_names(names: iter[str]) -> set[str]:
        unique_names = {name.strip().capitalize() for name in names}
        if len(names) != len(unique_names):
            logging.warning("There are duplicate names.")
        return unique_names

    @property
    def names(self) -> tuple[str]:
        return self._names
    
    @property
    def scores(self) -> dict[str, int]:
        return self._scores
    
    @property
    def rounds_won(self) -> dict[str, int]:
        return self._rounds_won
    
    @property
    def games_won(self) -> dict[str, int]:
        return self._rounds_won
    
    @classmethod
    def from_players(cls, players: iter[Player]) -> ScoreBoard:
        names = tuple(p.name for p in players)
        return cls(names)

    def is_registered(self, name: str) -> bool:
        return name in self.names

    def register(self, name: str) -> None:
        if self.is_registered(name):
            raise KeyError(f"{name} is already on the scoreboard.")
        self.scores[name] = 0
        self.rounds_won[name] = 0
        logging.info(f"{name} added to the scoreboard.")

    def get_score_of(self, name: str) -> int | None:
        if not self.is_registered(name):
            raise KeyError(f"{name} not registered -> could not get score.")
        return self.scores[name]

    def increment_score_of(self, name: str, value: int) -> None:
        if not self.is_registered(name):
            raise KeyError(f"{name} not registered -> could not increase score.")
        self.scores[name] += value

    def increment_rounds_of(self, name: str) -> None:
        if not self.is_registered(name):
            raise KeyError(f"{name} not registered -> could not increment rounds won.")
        self.rounds_won[name] += 1

    def get_game_winners(self) -> tuple[str] | None:
        highest_score = max(self.scores.values())
        score_leaders = tuple(name for name in self.names if self.scores[name] == highest_score)
        if len(score_leaders) > 1:
            return self.resolve_tie_with_rounds(score_leaders)
        return score_leaders

    def resolve_tie_with_rounds(self, names: tuple[str]) -> tuple[str]:
        name_to_rounds_won = {n: self.rounds_won[n] for n in names}
        highest_nb_rounds_won = max(self.rounds_won.values())
        winners = tuple(
            p for p, r in name_to_rounds_won.items() if r == highest_nb_rounds_won
        )
        unresolvable_tie = len(winners) > 1 and len(self.names) == 2        
        if unresolvable_tie:
            return tuple()
        return winners

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
    scoreboard.increment_score_of(players[1].name, value=100)
    print(scoreboard)
    scoreboard.increment_score_of(players[1].name, value=50)
    print(scoreboard)
    scoreboard.increment_rounds_of(players[1].name)
    print(scoreboard)
