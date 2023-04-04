from typing import Protocol

from card import Pile
from player import Player

SEPARATOR = "~"


class UI(Protocol):

    @staticmethod
    def render_round_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_game_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        ...

    @staticmethod
    def render_player_card(player: Player) -> None:
        ...

    @staticmethod
    def render_pile(pile: Pile, separator: bool = False) -> None:
        ...

    @staticmethod
    def render_msg(msg: str) -> None:
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
    def render_scoreboard(player: Player, other_player: Player) -> None:
        msg = f"Score is: {player.name} {player.score} - {other_player.score} {other_player.name}"
        stream = "\n".join([SEPARATOR * len(msg), msg, SEPARATOR * len(msg)])
        print(stream)

    @staticmethod
    def render_player_card(player: Player) -> None:
        print(f"{player.name} picked {player.card.name}.")

    @staticmethod
    def render_pile(pile: Pile, separator: bool = False) -> None:
        if pile.cards:
            cards = [card.name for card in pile.cards]
            msg = f"The {pile.name} pile is: {cards}"
        else:
            msg = f"The {pile.name} pile is empty."
        print(msg)
        if separator:
            print(SEPARATOR)

    @staticmethod
    def render_msg(msg: str) -> None:
        print(msg)
