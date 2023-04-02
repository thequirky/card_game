from dataclasses import dataclass

from card import Card


@dataclass
class PlayerType:
    name: str
    score: int = 0  # TODO: refactor to round score and introduce Scoreboard for scores across all games
    card_held: Card = Card.NO_CARD


class Player(PlayerType):
    def get_score(self) -> int:
        return self.score

    def get_card(self) -> Card:
        return self.card

    def get_name(self) -> str:
        return self.name

    def increase_score_by(self, value: int):
        self.score += value

    def reset_score(self) -> None:
        self.score = 0

    def put_down_card(self) -> Card:
        removed_card = self.card
        self.card = Card.NO_CARD
        return removed_card

    def pick_up_card(self, card: Card) -> None:
        self.card = card


if __name__ == "__main__":
    evan = Player(name="evan")
    print(evan)
    evan.name = "Evan"
    evan.increase_score_by(2)
    evan.pick_up_card(card=Card.ACE)
    print(evan)
    evan.put_down_card()
    print(evan)
    print(evan.get_score())
    evan.reset_score()
    print(evan.get_score())
