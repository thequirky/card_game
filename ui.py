from dataclasses import dataclass
from enum import Enum
from typing import Protocol


class Card(Enum):
    ...


@dataclass
class Pile(Protocol):

    def name(self) -> list[Card]:
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
    def show_round_winner(self, player: Player) -> None:
        ...

    @staticmethod
    def show_game_winner(self, player: Player) -> None:
        ...

    def show_scoreboard(self, player: Player, other_player: Player) -> None:
        ...

    @staticmethod
    def show_player_card(self, player: Player) -> None:
        ...

    def show_pile(self, pile: Pile, separator: bool = False) -> None:
        ...


class CLI:

    @staticmethod
    def show_round_winner(player: Player) -> None:
        if player:
            print(f"Round winner is {player.name}.")
        else:
            print("Round is a tie.")

    @staticmethod
    def show_game_winner(player: Player) -> None:
        if player:
            msg = f"Game winner is {player.name}!"
        else:
            msg = "Game is a tie!"
        print(msg)

    @staticmethod
    def _show_separator() -> None:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def show_scoreboard(self, player: Player, other_player: Player) -> None:
        msg = f"{player.name} {player.score} - {other_player.score} {other_player.name}"
        self._show_separator()
        print(msg)
        self._show_separator()

    @staticmethod
    def show_player_card(player: Player) -> None:
        print(f"{player.name} picked {player.card.value.capitalize()}.")

    def show_pile(self, pile: Pile, separator: bool = False) -> None:
        if pile.cards:
            cards = [card.name.capitalize() for card in pile.cards]
            msg = f"The {pile.name} pile is: {cards}"
        else:
            msg = f"The {pile.name} pile is empty."
        print(msg)
        if separator:
            self._show_separator()
