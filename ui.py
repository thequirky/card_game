from typing import Protocol

from card import Pile
from player import Player

SEPARATOR = "~"
PADDING = " " * 3
ENDER = "|"


class UI(Protocol):

    @staticmethod
    def render_round_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_game_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_scoreboard(player: Player, other_player: Player) -> None:
        ...

    @staticmethod
    def render_player_cards(players: tuple[Player, Player]) -> None:
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
            msg = f"\n{player.name} wins the game!!!"
        print(msg)

    def as_banner(self, msg: str) -> str:
        new_msg = PADDING.join([ENDER, msg, ENDER])
        new_msg = "\n".join([SEPARATOR * len(new_msg), new_msg, SEPARATOR * len(new_msg)])
        return new_msg

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        msg = f"{player.name} {player.score} - {other_player.score} {other_player.name}"
        msg = self.as_banner(msg=msg)
        print(msg)

    @staticmethod
    def render_player_cards(players: tuple[Player, Player]) -> None:
        msg = " ".join([f"{player.name} picked {player.card.name}." for player in players])
        print(msg)

    @staticmethod
    def render_pile(pile: Pile, separator: bool = False) -> None:
        if not pile.cards:
            msg = f"The {pile.name} pile is empty."
        else:
            cards = [card.name for card in pile.cards]
            msg = f"The {pile.name} pile is: {cards}"
        if separator:
            msg = "\n".join([msg, SEPARATOR * len(msg)])
        print(msg)

    @staticmethod
    def render_msg(msg: str) -> None:
        print(msg)
