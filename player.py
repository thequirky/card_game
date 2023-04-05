from dataclasses import dataclass

from card import Card


@dataclass
class Player:
    name: str
    score: int = 0
    rounds_won: int = 0  # not used yet
    card: Card | None = None

    # TODO: implement Scoreboard that registers players and keeps track of round and game scores

    def increase_score_by(self, value: int):
        self.score += value

    def reset_score(self) -> None:
        self.score = 0

    def put_down_card(self) -> Card:
        removed_card = self.card
        self.card = None
        return removed_card

    def pick_up_card(self, card: Card) -> None:
        self.card = card


if __name__ == "__main__":
    evan = Player(name="evan")
    print(evan)
    evan.name = "Evan"
    evan.increase_score_by(2)
    evan.pick_up_card(card=Card.Ace)
    print(evan)
    evan.put_down_card()
    print(evan)
    print(evan.score)
    evan.reset_score()
    print(evan.score)
