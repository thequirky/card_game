from dataclasses import dataclass, field


@dataclass
class ScoreBoard:
    scores: dict[str, int] = field(default_factory=dict)  # {name: score}
    rounds_won: dict[str, int] = field(default_factory=dict)  # {name: rounds_won}

    @property
    def player_names(self) -> tuple[str]:
        return tuple(self.scores.keys())

    # todo: maybe replace registration with cls instantion from player names
    def register_player(self, name: str) -> None:
        if name in self.player_names:
            print(f"{name} is already on the scoreboard!")
            return
        self.scores[name] = 0
        self.rounds_won[name] = 0
        print(f"{name} was added to the scoreboard.")

    def is_registered(self, name: str) -> bool:
        if name not in self.player_names:
            print(f"{name} is not registered on the scoreboard...")
            return False
        return True

    def get_score_of(self, player_name: str) -> int:
        if self.is_registered(player_name):
            return self.scores[player_name]

    def increase_player_score_by(self, player_name: str, value: int) -> None:
        if self.is_registered(player_name):
            self.scores[player_name] += value

    def increment_player_rounds_won(self, player_name: str) -> None:
        if self.is_registered(player_name):
            self.rounds_won[player_name] += 1

    def reset_scores(self) -> None:
        self.scores = {k: 0 for k in self.scores}

    def reset_rounds(self) -> None:
        self.rounds_won = {k: 0 for k in self.rounds_won}

    # todo: add string representation
    # def __str__(self) -> str:
    #     return

if __name__ == "__main__":
    from player import Player

    scoreboard = ScoreBoard()
    print(scoreboard)
    p1 = Player("evan")
    p2 = Player("viola")
    p3 = Player("viola")
    scoreboard.register_player(p1.name)
    scoreboard.register_player(p2.name)
    scoreboard.register_player(p3.name)
    print(scoreboard)
    scoreboard.increase_player_score_by(player_name=p2.name, value=100)
    print(scoreboard)
    scoreboard.increase_player_score_by(player_name="unknown", value=50)
    scoreboard.increment_player_rounds_won(p2.name)
    print(scoreboard)
    scoreboard.reset_scores()
    print(scoreboard)
