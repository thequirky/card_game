from typing import Protocol

from deck import Deck
from player import Player


class UI(Protocol):

    def show_round_winner(self, player: Player) -> None:
        ...

    def show_game_winner(self, player: Player) -> None:
        ...

    def show_scoreboard(self, player: Player, other_player: Player) -> None:
        ...

    def show_player_card(self, player: Player) -> None:
        ...

    def show_cards_pile(self, deck: Deck) -> None:
        ...

    def show_removed_cards_pile(self, deck: Deck) -> None:
        ...


class CLI:

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

    def show_player_card(self, player: Player) -> None:
        print(f"{player.name} picked {player.card_held.value.capitalize()}.")

    def show_cards_pile(self, deck: Deck, separator: bool = False) -> None:
        if deck.pile:
            deck_cards = [card.name.capitalize() for card in deck.pile]
            msg = f"Deck is: {deck_cards}"
        else:
            msg = "The deck pile is empty."
        print(msg)
        if separator:
            self._show_separator(length=len(msg))

    def show_removed_cards_pile(self, deck: Deck) -> None:
        if deck.removed_pile:
            removed_cards = [card.name.capitalize() for card in deck.removed_pile]
            print(f"The removed cards pile is: {removed_cards}.")
        else:
            print("The removed cards pile is empty.")
