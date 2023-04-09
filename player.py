from card import Card


class Player:
    name: str
    card: Card | None = None

    def __init__(self, name) -> None:
        self._name = name.capitalize()

    @property
    def name(self) -> str:
        return self._name

    @property
    def holds_card(self) -> bool:
        return bool(self.card)

    def discard(self) -> Card:
        if not self.holds_card:
            raise Exception(f"{self.name} has no card to put down...")
        discarded = self.card
        self.card = None
        # print(f"{self.name} discarded {discarded_card} and now has no card.")
        return discarded

    def pick_up_card(self, card: Card) -> None:
        if self.holds_card:
            raise Exception(f"{self.name} could not pick up {card}, already holds {self.card}...")
        self.card = card
        # print(f"{self.name} picked up {card}.")

    def __str__(self):
        if not self.holds_card:
            return f"{self.name} holds no card."
        return f"{self.name} holds {self.card}."


if __name__ == "__main__":
    # player = Player()  # raises exception -> must provide name
    player = Player("evan")
    print(player)
    # player.discard()  # raises exception -> no card to discard
    player.pick_up_card(Card.Ace)
    # player.pick_up_card(Card.Joker)  # raises exception -> already holding card
    print(player)
    player.discard()
    print(player)
