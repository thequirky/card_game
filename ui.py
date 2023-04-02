from typing import Protocol

from card import Pile
from player import Player


class UI(Protocol):
    # TODO: remove reliance on player and deck knowledge
    def show_round_winner(self, player: Player) -> None:
        ...

    def show_game_winner(self, player: Player) -> None:
        ...

    def show_scoreboard(self, player: Player, other_player: Player) -> None:
        ...

    def show_player_card(self, player: Player) -> None:
        ...

    def show_pile(self, pile: Pile, pile_type: str, separator: bool = False) -> None:
        ...


class CLI:  # TODO: maybe remove reliance on player knowledge ?

    def show_round_winner(self, player: Player) -> None:
        if player:
            print(f"Round winner is {player.name}.")
        else:
            print("Round is a tie.")

    def show_game_winner(self, player: Player) -> None:
        if player:
            print(f"Game winner is {player.name}!")
        else:
            print("Game is a tie!")

    @staticmethod
    def _show_separator(length: int = 10) -> None:
        print("=" * length)

    def show_scoreboard(self, player: Player, other_player: Player) -> None:
        msg = f"{player.name} has {player.score} score points. {other_player.name} has {other_player.score} score points."
        self._show_separator(length=len(msg))
        print(msg)
        self._show_separator(length=len(msg))

    @staticmethod
    def show_player_card(player: Player) -> None:
        print(f"{player.name} picked {player.card.value.capitalize()}.")

    def show_pile(self, pile: Pile, pile_type: str, separator: bool = False) -> None:
        if pile.cards:
            cards = [card.name.capitalize() for card in pile.cards]
            msg = f"The {pile.name} pile is: {cards}"
        else:
            msg = f"The {pile.name} pile is empty."
        print(msg)
        if separator:
            self._show_separator(length=len(msg))
