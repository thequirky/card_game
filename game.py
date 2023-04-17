from card import Pile
from player import Player
from scoreboard import ScoreBoard
from ui import UI
import logging


class CardGame:
    def __init__(
        self,
        players: tuple[Player],
        game_pile: Pile,
        discard_pile: Pile,
        ui: UI,
        scoreboard: ScoreBoard,
    ) -> None:
        self.game_pile = game_pile
        self.discard_pile = discard_pile
        self.players = players
        self.ui = ui
        self.scoreboard = scoreboard

    def get_round_winners(self) -> tuple[Player] | None:
        player_to_hand_value = {p: p.hand.value for p in self.players}
        unique_values = set(player_to_hand_value.values())
        all_players_hold_same_card = len(unique_values) == 1
        if all_players_hold_same_card:
            return
        max_value = max(unique_values)
        winners = tuple(p for p, v in player_to_hand_value.items() if v == max_value)
        return winners

    def deal_random(self) -> None:
        for player in self.players:
            picked = self.game_pile.draw_random()
            player.hold(picked)

    def discard_all(self) -> None:
        for player in self.players:
            discarded = player.discard()
            self.discard_pile.add(discarded)

    def update_scoreboard(self) -> None:
        winners = self.get_round_winners()
        if not winners:
            return
        for winner in winners:
            self.scoreboard.increment_score_of(name=winner.name, value=winner.hand.value)
            self.scoreboard.increment_rounds_of(winner.name)

    def more_players_than_cards(self) -> bool:
        return len(self.players) > len(self.game_pile.cards)

    def reshuffle(self) -> None:
        self.game_pile.reshuffle(self.discard_pile)
        self.discard_pile.cards = []

    def max_nb_rounds_without_reshuffle(self) -> int:
        return len(self.game_pile.cards) // len(self.players)

    def names_to_players(self, names: tuple[str]) -> tuple[Player] | None:
        return tuple(p for p in self.players if p.name in names) if names else None

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

    def run(self, nb_rounds: int | None = None) -> None:
        if not nb_rounds:
            # keep doing rounds until cards run out
            nb_rounds = self.max_nb_rounds_without_reshuffle()

        self.ui.render_pile(self.game_pile)
        self.ui.render_pile(self.discard_pile)

        for round_nb in range(nb_rounds):
            self.ui.render_msg(f"\nRound {round_nb + 1}:")

            if self.game_pile.is_empty():
                logging.info("No more cards left to pick from -> reshuffling")
                self.reshuffle()

            elif self.more_players_than_cards():
                logging.info("Not enough cards in the pile for all players -> reshuffling")
                self.reshuffle()

            self.do_round()

        names_of_game_winners = self.scoreboard.get_game_winners()
        winners = self.names_to_players(names_of_game_winners)
        self.ui.render_game_winners(winners)


if __name__ == "__main__":
    from ui import CLI

    logging.basicConfig(level=logging.WARNING)

    player1 = Player("evan")
    player2 = Player("viola")
    scoreboard = ScoreBoard(["evan", "viola"])
    game_pile = Pile.from_seed(seed="AKKQQQJJJJ", name="game")
    discard_pile = Pile("discard")
    cli = CLI()
    game = CardGame(
        players=(player1, player2),
        game_pile=game_pile,
        discard_pile=discard_pile,
        ui=cli,
        scoreboard=scoreboard,
    )

    game.run(10)
