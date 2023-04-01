from enum import Enum


class Card(Enum):
    ACE = "ace"
    KING = "king"
    QUEEN = "queen"
    NO_CARD = ""


CARD_VALUE = {
    Card.ACE: 3,
    Card.KING: 2,
    Card.QUEEN: 1,
    Card.NO_CARD: 0,
}

if __name__ == "__main__":
    example_card = Card.QUEEN
    print(example_card)
    print(type(example_card))
    print(CARD_VALUE[example_card])

    example_card_lst = [Card.QUEEN, Card.KING]
    print(example_card_lst)
    print(type(example_card_lst))
