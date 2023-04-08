from typing import Protocol

from card import Pile
from player import Player
from scoreboard import ScoreBoard


class UI(Protocol):

    @staticmethod
    def render_round_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_game_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_scoreboard(self, scoreboard: ScoreBoard) -> None:
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

    @staticmethod
    def render_scoreboard(scoreboard: ScoreBoard) -> None:
        print(scoreboard)

    @staticmethod
    def render_pile(pile: Pile) -> None:
        if not pile.cards:
            msg = f"The {pile.name} pile is empty."
        else:
            cards = [card.name for card in pile.cards]
            msg = f"The {pile.name} pile is: {cards}"
        print(msg)

    @staticmethod
    def render_player_cards(players: tuple[Player, Player]) -> None:
        msg = " ".join([f"{player.name} picked {player.card.name}." for player in players])
        print(msg)

    @staticmethod
    def render_msg(msg: str) -> None:
        print(msg)
