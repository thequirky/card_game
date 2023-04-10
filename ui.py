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
