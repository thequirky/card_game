from typing import Protocol

from card import Pile
from player import Player


SEPARATOR = "~" * 80


class UI(Protocol):

    @staticmethod
    def render_round_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_game_winner(player: Player) -> None:
        ...

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        ...

    @staticmethod
    def render_player_card(player: Player) -> None:
        ...

    def render_pile(self, pile: Pile, separator: bool = False) -> None:
        ...

    @staticmethod
    def render_msgs(msgs: str | list[str]) -> None:
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

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        msg = f"{player.name} {player.score} -- {other_player.score} {other_player.name}"
        print(SEPARATOR)
        print(msg)
        print(SEPARATOR)

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
            print(SEPARATOR)

    @staticmethod
    def render_msgs(msgs: str | list[str]) -> None:
        print(" ".join(msgs))
