from enum import Enum
from typing import Protocol


class Card(Enum):
    ...


class Pile:
    name: str
    cards: list[Card]


class Player:
    name: str
    score: int
    card: Card


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
        print("~" * 69)

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        msg = f"{player.name} {player.score} - {other_player.score} {other_player.name}"
        self._render_separator()
        print(msg)
        self._render_separator()

    @staticmethod
    def render_player_card(player: Player) -> None:
        print(f"{player.name} picked {player.card.value}.")

    def render_pile(self, pile: Pile, separator: bool = False) -> None:
        if pile.cards:
            cards = [card.value for card in pile.cards]
            msg = f"The {pile.name} pile is: {cards}"
        else:
            msg = f"The {pile.name} pile is empty."
        print(msg)
        if separator:
            self._render_separator()
