from dataclasses import dataclass, field
from player import Player


@dataclass
class ScoreBoard:
    players: list[str] = field(default_factory=list)
    scores: dict[str, int] = field(default_factory=dict)  # dict with player_name: str as key and score: int as value
    rounds_won: dict[str, int] = field(
        default_factory=dict)  # dict with player_name: str as key and rounds_won: int as value

    def register_player(self, player_name: str) -> None:
        self.scores[player_name] = 0
        self.rounds_won[player_name] = 0

    def is_registered(self, player_name: str) -> bool:
        if player_name not in self.scores.keys():
            print(f"{player_name} is not registered on the scoreboard.")
            return False
        return True

    def update_score(self, player_name: str, score: int) -> None:
        if self.is_registered(player_name):
            self.scores[player_name] = score

    def increase_player_score_by(self, player_name: str, value: int) -> None:
        if self.is_registered(player_name):
            self.scores[player_name] = value

    def player_wins_round(self, player_name: str) -> None:
        if self.is_registered(player_name):
            self.rounds_won[player_name] += 1

    def reset_scores(self) -> None:
        self.scores = {k: 0 for k in self.scores}

    def reset_rounds(self) -> None:
        self.rounds_won = {k: 0 for k in self.rounds_won}


if __name__ == "__main__":
    sb = ScoreBoard()
    print(sb)
    p1 = Player(name="evan")
    p2 = Player(name="viola")
    sb.register_player(player_name=p1.name)
    sb.register_player(player_name=p2.name)
    print(sb)
    sb.increase_player_score_by(player_name=p2.name, value=100)
    print(sb)
    sb.increase_player_score_by(player_name="someone else", value=50)
    sb.update_score(player_name=p1.name, score=50)
    print(sb)
    sb.player_wins_round(player_name=p2.name)
    print(sb)
    sb.reset_scores()
    print(sb)
