from typing import Protocol

from card import Pile
from player import Player


class UI(Protocol):
    @staticmethod
    def render_round_winner(players: tuple[Player] | None) -> None:
        ...

    @staticmethod
    def render_game_winners(players: tuple[Player] | None) -> None:
        ...

    @staticmethod
    def render_scoreboard(scoreboard: str) -> None:
        ...

    @staticmethod
    def render_hands(players: tuple[Player]) -> None:
        ...

    @staticmethod
    def render_pile(pile: Pile) -> None:
        ...

    @staticmethod
    def render_msg(msg: str) -> None:
        ...


class CLI:
    @staticmethod
    def render_round_winner(players: tuple[Player] | None) -> None:
        if not players:
            msg = "Round is a tie..."
        elif len(players) == 1:
            msg = f"Round winner is {players[0].name}!"
        else:
            winners = ", ".join([player.name for player in players])
            msg = f"Round winners are {winners}!"
        print(msg)

    @staticmethod
    def render_game_winners(players: tuple[Player] | None) -> None:
        if not players:
            msg = "\n!!! The game is a tie !!!\n"
        else:
            winners = ", ".join([player.name for player in players])
            msg = f"\n!!! {winners} won the game !!!\n"
        print(msg)

    @staticmethod
    def render_scoreboard(scoreboard: str) -> None:
        msg = scoreboard
        print(msg)

    @staticmethod
    def render_pile(pile: Pile) -> None:
        if not pile.cards:
            msg = f"The {pile.name.lower()} pile is now empty."
        else:
            msg = pile
        print(msg)

    @staticmethod
    def render_hands(players: tuple[Player]) -> None:
        msg = ", ".join([f"{p.name} drew -> {p.hand}" for p in players])
        print(msg)

    @staticmethod
    def render_msg(msg: str) -> None:
        print(msg)
