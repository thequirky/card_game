from dataclasses import dataclass

from card import Card


@dataclass
class Player:
    name: str
    card: Card | None = None

    def puts_down_card(self) -> Card:
        removed_card = self.card
        self.card = None
        return removed_card

    def picks_up_card(self, card: Card) -> None:
        self.card = card

    def __str__(self):
        if not self.card:
            return f"{self.name} holds no card."
        return f"{self.name} holds {self.card.name}."


if __name__ == "__main__":
    evan = Player(name="Evan")
    print(evan)
    evan.picks_up_card(card=Card.Ace)
    print(evan)
    evan.puts_down_card()
    print(evan)
