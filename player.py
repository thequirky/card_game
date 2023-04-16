from __future__ import annotations

from card import Card


class Player:
    hand: Card | None = None

    def __init__(self, name) -> None:
        self._name = name.strip().capitalize()

    @property
    def name(self) -> str:
        return self._name

    @classmethod
    def from_names(cls, names: list[str]) -> tuple[Player]:
        return tuple(cls(name) for name in names)

    @property
    def is_holding(self) -> bool:
        return bool(self.hand)

    def discard(self) -> Card:
        if not self.is_holding:
            raise Exception(f"{self.name} has no card to discard.")
        discarded = self.hand
        self.hand = None
        return discarded

    def hold(self, card: Card) -> None:
        if self.is_holding:
            raise Exception(
                f"{self.name} could not pick up {card} -> already holds {self.hand}."
            )
        self.hand = card

    def __str__(self):
        if not self.is_holding:
            return f"{self.name} holds no card."
        return f"{self.name} holds {self.hand}."


if __name__ == "__main__":
    player = Player("evan")
    print(player)
    player.hold(Card.Ace)
    print(player)
    player.is_holding  # True
    player.discard()
    player.is_holding  # False
