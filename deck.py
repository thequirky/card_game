import random
from dataclasses import dataclass, field

from card import Card

STR_TO_CARD = {"a": Card.ACE, "k": Card.KING, "q": Card.QUEEN}


@dataclass
class Deck:
    """Deck consists of a cards pile and a removed cards pile"""
    # TODO: Maybe make pile a Deck and removed_pile another Deck to reduce number of methods
    pile: list[Card] = field(default_factory=list)
    removed_pile: list[Card] = field(default_factory=list)

    @classmethod
    def from_str(cls, card_string: str, shuffle: bool = False):
        new_pile = [STR_TO_CARD[s] for s in card_string]
        if shuffle:
            random.shuffle(new_pile)
        return cls(pile=new_pile)

    def pick_card_from_top_of_pile(self) -> Card:
        if self.pile:
            picked_card = self.pile.pop()
            if self.removed_pile:
                self.removed_pile.append(picked_card)
            else:
                self.removed_pile = [picked_card]
            return picked_card

    def pick_random_card_from_pile(self) -> Card:
        if self.pile:
            random_idx = random.randint(0, len(self.pile) - 1)
            picked_card = self.pile.pop(random_idx)
            if self.removed_pile:
                self.removed_pile.append(picked_card)
            else:
                self.removed_pile = [picked_card]
            return picked_card

    def shuffle_cards_pile(self, times: int = 1) -> None:
        if self.pile:
            for _ in range(times):
                random.shuffle(self.pile)

    def shuffle_removed_cards_pile(self, times: int = 1) -> None:
        if self.removed_pile:
            for _ in range(times):
                random.shuffle(self.removed_pile)

    def shuffle_all_cards_together(self, times: int = 1) -> None:
        self.put_removed_cards_on_top_of_pile()
        self.shuffle_cards_pile(times=times)

    def put_removed_cards_on_top_of_pile(self) -> None:
        if not self.pile:
            self.pile = self.removed_pile
            self.removed_pile = None
        else:
            self.pile.extend(self.removed_pile)
            self.removed_pile = None

    def add_card_to_top_of_pile(self, card: Card) -> None:
        self.pile.append(card)


if __name__ == "__main__":
    from ui import CLI

    deck = Deck.from_str(card_string="aaakkkqqq", shuffle=True)
    cli = CLI()

    print("Starting deck:")
    cli.show_cards_pile(deck=deck)
    cli.show_removed_cards_pile(deck=deck)
    print("\n")

    deck.shuffle_cards_pile()
    print("After shuffling:")
    cli.show_cards_pile(deck=deck)
    cli.show_removed_cards_pile(deck=deck)
    print("\n")

    picked = deck.pick_card_from_top_of_pile()
    print("After picking the card from the top of the pile:")
    print("Picked: ", picked.name.capitalize())
    cli.show_cards_pile(deck=deck)
    cli.show_removed_cards_pile(deck=deck)
    print("\n")

    picked = deck.pick_card_from_top_of_pile()
    print("After picking another card from the top of the pile:")
    print("Picked: ", picked.name.capitalize())
    cli.show_cards_pile(deck=deck)
    cli.show_removed_cards_pile(deck=deck)
    print("\n")

    picked = deck.pick_random_card_from_pile()
    print("After picking a random card from the pile:")
    print("Picked: ", picked.name.capitalize())
    cli.show_cards_pile(deck=deck)
    cli.show_removed_cards_pile(deck=deck)
    print("\n")

    picked = deck.pick_random_card_from_pile()
    print("After picking another random card:")
    print("Picked: ", picked.name.capitalize())
    cli.show_cards_pile(deck=deck)
    cli.show_removed_cards_pile(deck=deck)
    print("\n")

    deck.put_removed_cards_on_top_of_pile()
    print("After putting removed cards back on top:")
    cli.show_cards_pile(deck=deck)
    cli.show_removed_cards_pile(deck=deck)
    print("\n")
