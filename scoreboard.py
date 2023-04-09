from __future__ import annotations

from dataclasses import dataclass, field

from ui import UI


@dataclass
class ScoreBoard:
    ui: UI | None = field(default=None, repr=False)
    scores: dict[str, int] = field(default_factory=dict)  # {name: score}
    rounds_won: dict[str, int] = field(default_factory=dict)  # {name: rounds_won}

    @property
    def player_names(self) -> tuple[str]:
        return tuple(self.scores.keys())

    @classmethod
    def from_player_names(cls, names: list[str], ui: UI = None) -> ScoreBoard:
        scoreboard = cls(ui=ui)
        for name in names:
            if name in scoreboard.scores.keys():
                if ui:
                    ui.render_msg(f"{name} is already on the scoreboard!")
                continue
            scoreboard.scores[name] = 0
            scoreboard.rounds_won[name] = 0
            ui.render_msg(f"{name} was added to the scoreboard.") and ui
        return scoreboard

    def register_player(self, name: str) -> None:
        if name in self.player_names:
            self.ui.render_msg(f"{name} is already on the scoreboard!") and self.ui
            return
        self.scores[name] = 0
        self.rounds_won[name] = 0
        self.ui.render_msg(f"{name} was added to the scoreboard.")

    def is_registered(self, name: str) -> bool:
        if name not in self.player_names:
            self.ui.render_msg(f"{name} is not registered on the scoreboard...") and self.ui
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

    # todo: add custom string representation
    # def __str__(self) -> str:
    #     return

if __name__ == "__main__":
    from player import Player
    from ui import CLI

    cli = CLI()
    p1 = Player("evan")
    p2 = Player("viola")
    p3 = Player("viola")
    names = [p1.name, p2.name, p3.name]
    scoreboard = ScoreBoard.from_player_names(names=names, 
                                              ui=cli)  # verbose if ui is provided
    # scoreboard = ScoreBoard.from_player_names(names)
    scoreboard.register_player(p1.name)
    print(scoreboard)
    scoreboard.increase_player_score_by(player_name=p2.name, value=100)
    print(scoreboard)
    scoreboard.increase_player_score_by(player_name="unknown", value=50)
    scoreboard.increment_player_rounds_won(p2.name)
    print(scoreboard)
    scoreboard.reset_scores()
    print(scoreboard)
