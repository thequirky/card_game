from __future__ import annotations

from card import Card


class Player:
    def __init__(self, name) -> None:
        self._name = name.strip().capitalize()
        self.hand: Card = None

    @property
    def name(self) -> str:
        return self._name

    @classmethod
    def from_names(cls, names: iter[str]) -> tuple[Player]:
        unique_names = {n.strip().capitalize() for n in names}
        if len(unique_names) != len(names):
            raise ValueError("Duplicate names found.")
        return tuple(cls(name) for name in unique_names)

    def discard(self) -> Card:
        if not self.hand:
            raise Exception(f"{self.name} has no card to discard.")
        discarded = self.hand
        self.hand = None
        return discarded

    def hold(self, card: Card) -> None:
        if self.hand:
            raise Exception(
                f"{self.name} could not pick up {card} -> already holds {self.hand}."
            )
        self.hand = card

    def __str__(self):
        if not self.hand:
            return f"{self.name} holds no card."
        return f"{self.name} holds {self.hand}."

    def __repr__(self) -> str:
        return f'Player(name="{self.name}", hand=Card.{self.hand})'


if __name__ == "__main__":
    player = Player("evan")
    player.hold(Card.Ace)
    player.discard()
    print(player)

