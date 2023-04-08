from dataclasses import dataclass, field


@dataclass
class ScoreBoard:
    scores: dict[str, int] = field(default_factory=dict)        # dict with player_name: str as key and score: int as value
    rounds_won: dict[str, int] = field(default_factory=dict)    # dict with player_name: str as key and rounds_won: int as value

    @property
    def player_names(self):
        return self.scores.keys()

    def register_player(self, player_name: str) -> None:
        if player_name in self.player_names:
            print(f"{player_name} is already registed on the scoreboard.")
            return
        self.scores[player_name] = 0
        self.rounds_won[player_name] = 0

    def is_registered(self, player_name: str) -> bool:
        if player_name not in self.player_names:
            print(f"{player_name} is not registered on the scoreboard.")
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


if __name__ == "__main__":
    from player import Player

    scoreboard = ScoreBoard()
    print(scoreboard)
    evan = Player(name="Evan")
    viola = Player(name="Viola")
    unknown = Player(name="Viola")
    scoreboard.register_player(player_name=evan.name)
    scoreboard.register_player(player_name=viola.name)
    scoreboard.register_player(player_name=unknown.name)
    print(scoreboard)
    scoreboard.increase_player_score_by(player_name=viola.name, value=100)
    print(scoreboard)
    scoreboard.increase_player_score_by(player_name="Unknown", value=50)
    scoreboard.increment_player_rounds_won(player_name=viola.name)
    print(scoreboard)
    scoreboard.reset_scores()
    print(scoreboard)
