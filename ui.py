from dataclasses import dataclass, field
from enum import IntEnum, auto
from typing import Protocol

from card import Pile
from player import Player


class UI(Protocol):
    @staticmethod
    def render_round_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_game_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_scoreboard(scoreboard: str) -> None:
        ...

    @staticmethod
    def render_player_cards(players: tuple[Player, Player]) -> None:
        ...

    @staticmethod
    def render_pile(pile: Pile) -> None:
        ...

    @staticmethod
    def render_msg(msg: str) -> None:
        ...


class CLI:
    @staticmethod
    def render_round_winner(player: Player) -> None:
        if not player:
            msg = "Round is a tie..."
        else:
            msg = f"Round winner is {player.name}!"
        print(msg)

    @staticmethod
    def render_game_winner(player: Player) -> None:
        if not player:
            msg = "\nGame is a tie...!"
        else:
            msg = f"\n!!! {player.name} wins the game !!!\n"
        print(msg)

    @staticmethod
    def render_scoreboard(scoreboard: str) -> None:
        msg = scoreboard
        print(msg)

    @staticmethod
    def render_pile(pile: Pile) -> None:
        if not pile.cards:
            msg = f"The {pile.name} pile is empty."
        else:
            msg = pile
        print(msg)

    @staticmethod
    def render_player_cards(players: tuple[Player, Player]) -> None:
        msg = " ".join([f"{p.name} picked {p.card}." for p in players])
        print(msg)

    @staticmethod
    def render_msg(msg: str) -> None:
        print(msg)


class LogLevels(IntEnum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    DEBUG = auto()


@dataclass
class Log:
    level: IntEnum
    data: list[tuple[IntEnum, str]] = field(default_factory=list)

    def log(self, level: IntEnum, msg: str) -> None:
        self.data.append((level, msg))
        if level <= self.level:
            print(f"{msg}")

    def show_all(self) -> None:
        for item in self.data:
            print(item)

    def __str__(self) -> str:
        new_str = []
        for level, msg, in self.data:
            new_str.append(f"{str(level.name)}: {msg}")
        return "\n".join(new_str)


if __name__ == "__main__":
    log_data = Log(level=LogLevels.ERROR)

    log_data.log(LogLevels.INFO, msg="This is an info log msg")
    log_data.log(LogLevels.WARNING, msg="This is a warning msg")
    log_data.log(LogLevels.ERROR, msg="This is an error log msg")
    log_data.log(LogLevels.DEBUG, msg="This is a debug msg")

    log_data.show_all()
    print(log_data)
