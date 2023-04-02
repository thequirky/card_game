from dataclasses import dataclass
from enum import Enum
from typing import Protocol


class Card(Enum):
    ...


@dataclass
class Pile(Protocol):

    def name(self) -> str:
        ...

    def cards(self) -> list[Card]:
        ...


@dataclass
class Player(Protocol):

    def name(self) -> str:
        ...

    def score(self) -> int:
        ...

    def card(self) -> Card:
        ...


class UI(Protocol):

    @staticmethod
    def render_round_winner(self, player: Player) -> None:
        ...

    @staticmethod
    def render_game_winner(self, player: Player) -> None:
        ...

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        ...

    @staticmethod
    def render_player_card(self, player: Player) -> None:
        ...

    def render_pile(self, pile: Pile, separator: bool = False) -> None:
        ...


class CLI:

    @staticmethod
    def render_round_winner(player: Player) -> None:
        if player:
            print(f"Round winner is {player.name}.")
        else:
            print("Round is a tie.")

    @staticmethod
    def render_game_winner(player: Player) -> None:
        if player:
            msg = f"Game winner is {player.name}!"
        else:
            msg = "Game is a tie!"
        print(msg)

    @staticmethod
    def _render_separator() -> None:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        msg = f"{player.name} {player.score} - {other_player.score} {other_player.name}"
        self._render_separator()
        print(msg)
        self._render_separator()

    @staticmethod
    def render_player_card(player: Player) -> None:
        print(f"{player.name} picked {player.card.value.capitalize()}.")

    def render_pile(self, pile: Pile, separator: bool = False) -> None:
        if pile.cards:
            cards = [card.name.capitalize() for card in pile.cards]
            msg = f"The {pile.name} pile is: {cards}"
        else:
            msg = f"The {pile.name} pile is empty."
        print(msg)
        if separator:
            self._render_separator()
