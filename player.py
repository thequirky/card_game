from card import Card


class Player:
    name: str
    card: Card | None = None

    def __init__(self, name) -> None:
        self._name = name.capitalize()

    @property
    def name(self):
        return self._name

    def puts_down_card(self) -> Card:
        removed_card = self.card
        self.card = None
        return removed_card

    def picks_up_card(self, card: Card) -> None:
        self.card = card

    def __str__(self):
        if not self.card:
            return f"{self.name} holds no card."
        return f"{self.name} holds {self.card}."


if __name__ == "__main__":
    # p1 = Player() will raise exception - must provide name
    p1 = Player("evan")
    print(p1)
    p1.picks_up_card(Card.Ace)
    print(p1)
    p1.puts_down_card()
    print(p1)
