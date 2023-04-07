from typing import Protocol

from card import Pile
from player import Player

SEPARATOR = "~"
PADDING = " " * 3
ENDER = "|"


# todo: add nice visualisation of cards and piles with ascii art
# todo: update render methods to return strings

class UI(Protocol):

    @staticmethod
    def render_round_winner(player: Player) -> None:
        ...

    @staticmethod
    def render_game_winner(player: Player) -> None:
        ...

    @staticmethod
    def as_banner(msg: str) -> str:
        ...

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
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
    def as_banner(msg: str) -> str:
        new_msg = PADDING.join([ENDER, msg, ENDER])
        new_msg = "\n".join([SEPARATOR * len(new_msg), new_msg, SEPARATOR * len(new_msg)])
        return new_msg

    def render_scoreboard(self, player: Player, other_player: Player) -> None:
        msg = f"{player.name} {player.score} - {other_player.score} {other_player.name}"
        msg = self.as_banner(msg=msg)
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
    def render_player_cards(players: tuple[Player, Player]) -> None:
        msg = " ".join([f"{player.name} picked {player.card.name}." for player in players])
        print(msg)

    @staticmethod
    def render_msg(msg: str) -> None:
        print(msg)


class AsciiArtCLI(CLI):

    @staticmethod
    def make_cards(ranks: list[str]) -> str:
        nb_cards = len(ranks)
        line1 = "".join(["┌────┐"] * nb_cards)
        line2 = "".join([f"│{rank}   │" for rank in ranks])
        line3 = "".join(["│    │"] * nb_cards)
        line4 = "".join(["└────┘"] * nb_cards)
        lines = [line1, line2, line3, line4]
        return "\n".join(lines)

    def render_pile(self, pile: Pile, separator: bool = False) -> None:
        if not pile.cards:
            msg = f"The {pile.name} pile is empty."
        else:
            card_ranks = [card.name[0].capitalize() for card in pile.cards]
            msg = self.make_cards(card_ranks)
        if separator:
            msg = "\n".join([msg, SEPARATOR * len(msg)])
        print(msg)

    def render_player_cards(self, players: tuple[Player, Player]) -> None:
        for player in players:
            rank = player.card.name[0].capitalize()
            msg = "\n".join([f"{player.name} picks:", self.make_cards(ranks=[rank])])
            print(msg)
