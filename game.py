import logging

from card.pile import Pile
from player import Player
from scoreboard import ScoreBoard
from ui import CLI


class CardGame:
    def __init__(self, players: list[Player], game_pile: Pile, ui: CLI, scoreboard: ScoreBoard) -> None:
        self.game_pile = game_pile
        self.players = players
        self.ui = ui
        self.scoreboard = scoreboard
        self.discard_pile = Pile("discard")

    def deal_random(self) -> None:
        for player in self.players:
            drawn_card = self.game_pile.draw_random()
            player.hold(drawn_card)

    def discard_all(self) -> None:
        for player in self.players:
            discarded = player.discard()
            self.discard_pile.add(discarded)

    def reshuffle(self) -> None:
        self.game_pile.reshuffle(self.discard_pile)
        self.discard_pile.cards = []

    def get_round_winners(self) -> list[Player]:
        max_value = max(p.hand.value for p in self.players)
        return [p for p in self.players if p.hand.value == max_value]

    def update_scoreboard(self) -> None:
        for winner in self.get_round_winners():
            self.scoreboard.increment_score(name=winner.name, value=winner.hand.value)
            self.scoreboard.increment_rounds(winner.name)

    def do_round(self) -> None:
        self.game_pile.shuffle()
        self.ui.render_pile(self.game_pile)
        self.deal_random()
        self.update_scoreboard()
        self.ui.render_hands(self.players)
        self.ui.render_round_winner(self.get_round_winners())
        self.discard_all()
        self.ui.render_pile(self.game_pile)
        self.ui.render_pile(self.discard_pile)
        self.ui.render_scoreboard(str(self.scoreboard))

    def run(self, nb_rounds: int = 0) -> None:
        nb_rounds = nb_rounds or len(self.game_pile.cards) // len(self.players)

        self.ui.render_pile(self.game_pile)
        self.ui.render_pile(self.discard_pile)

        for round_nb in range(nb_rounds):
            self.ui.render_msg(f"\nRound {round_nb + 1}:")
            more_players_than_cards_left = len(self.players) > len(self.game_pile.cards)

            if self.game_pile.is_empty():
                logging.info("No more cards left to pick from -> reshuffling")
                self.reshuffle()

            elif more_players_than_cards_left:
                logging.info("Not enough cards in the pile for all players -> reshuffling")
                self.reshuffle()

            self.do_round()

        names_won = self.scoreboard.get_game_winners()
        players_won = [p for p in self.players if p.name in names_won]
        self.ui.render_game_winners(players_won)
