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

    sb = ScoreBoard()
    print(sb)
    p1 = Player(name="Evan")
    p2 = Player(name="Viola")
    p3 = Player(name="Viola")
    sb.register_player(player_name=p1.name)
    sb.register_player(player_name=p2.name)
    sb.register_player(player_name=p3.name)
    print(sb)
    sb.increase_player_score_by(player_name=p2.name, value=100)
    print(sb)
    sb.increase_player_score_by(player_name="Someone else", value=50)
    sb.increment_player_rounds_won(player_name=p2.name)
    print(sb)
    sb.reset_scores()
    print(sb)
