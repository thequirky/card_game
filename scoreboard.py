from dataclasses import dataclass, field
from player import Player


@dataclass
class ScoreBoard:
    players: list[str] = field(default_factory=list)
    scores: dict[str, int] = field(default_factory=dict)

    def register_player(self, player: str) -> None:
        self.scores[player] = 0

    def update_score(self, player: str, score: int) -> None:
        if player not in self.scores.keys():
            print(f"{player} is not registered on the scoreboard.")
            return
        self.scores[player] = score


if __name__ == "__main__":
    sb = ScoreBoard()
    print(sb)
    pl1 = Player(name="evan")
    pl2 = Player(name="viola")
    sb.register_player(player=pl1.name)
    sb.register_player(player=pl2.name)
    print(sb)
    sb.update_score(player=pl2.name, score=100)
    print(sb)
    sb.update_score(player="someone", score=50)
