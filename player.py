from __future__ import annotations

from pile import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name = name.strip().capitalize()
        self.hand: Card | None = None

    @classmethod
    def from_names(cls, names: list[str]) -> list[Player]:
        return [cls(name) for name in names]

    def discard(self) -> Card:
        if not self.hand:
            raise ValueError(f"{self.name} has no card to discard.")
        discarded = self.hand
        self.hand = None
        return discarded

    def hold(self, card: Card) -> None:
        if self.hand:
            raise ValueError(f"{self.name} could not pick up {card} -> already holds {self.hand}.")
        self.hand = card

    def __str__(self) -> str:
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
