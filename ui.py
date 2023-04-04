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
    def _render_separator() -> None:
        ...

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        ...

    @staticmethod
    def render_player_card(player: Player) -> None:
        ...

    def render_pile(self, pile: Pile, separator: bool = False) -> None:
        ...

    @staticmethod
    def render_msg(msg) -> None:
        ...


class CLI:

    @staticmethod
    def render_round_winner(player: Player) -> None:
        if player:
            msg = f"Round winner is {player.name}."
        else:
            msg = "Round is a tie."
        print(msg)

    @staticmethod
    def render_game_winner(player: Player) -> None:
        if player:
            msg = f"Game winner is {player.name}!"
        else:
            msg = "Game is a tie!"
        print(msg)

    @staticmethod
    def _render_separator() -> None:
        print("~" * 80)

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        msg = f"{player.name} {player.score} -- {other_player.score} {other_player.name}"
        self._render_separator()
        print(msg)
        self._render_separator()

    @staticmethod
    def render_player_card(player: Player) -> None:
        print(f"{player.name} picked {player.card.name}.")

    def render_pile(self, pile: Pile, separator: bool = False) -> None:
        if pile.cards:
            cards = [card.name for card in pile.cards]
            msg = f"The {pile.name} pile is: {cards}"
        else:
            msg = f"The {pile.name} pile is empty."
        print(msg)
        if separator:
            self._render_separator()
