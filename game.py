from card import Pile
from player import Player
from scoreboard import ScoreBoard
from ui import UI
import logging


class CardActions:
    def __init__(
        self, players: tuple[Player], game_pile: Pile, discard_pile: Pile
    ) -> None:
        self.game_pile = game_pile
        self.discard_pile = discard_pile
        self.players = players

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


class GameActions:
    def __init__(self, players: tuple[Player], scoreboard: ScoreBoard) -> None:
        self.players = players
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

    def update_scoreboard(self) -> None:
        winners = self.get_round_winners()
        if not winners:
            return
        for winner in winners:
            self.scoreboard.increment_score_of(
                name=winner.name, value=winner.hand.value
            )
            self.scoreboard.increment_rounds_of(winner.name)


class CardGame:
    def __init__(
        self,
        players: tuple[Player],
        game_pile: Pile,
        discard_pile: Pile,
        ui: UI,
        scoreboard: ScoreBoard,
        game_actions: GameActions,
        card_actions: CardActions,
    ) -> None:
        self.game_pile = game_pile
        self.discard_pile = discard_pile
        self.players = players
        self.ui = ui
        self.scoreboard = scoreboard
        self.game_actions = game_actions
        self.card_actions = card_actions

    def do_round(self) -> None:
        self.game_pile.shuffle()
        self.ui.render_pile(self.game_pile)
        self.card_actions.deal_random()
        self.game_actions.update_scoreboard()
        self.ui.render_hands(self.players)
        self.ui.render_round_winner(self.game_actions.get_round_winners())
        self.card_actions.discard_all()
        self.ui.render_pile(self.game_pile)
        self.ui.render_pile(self.discard_pile)
        self.ui.render_scoreboard(str(self.scoreboard))

    def run(self, nb_rounds: int | None = None) -> None:
        if not nb_rounds:
            # keep doing rounds until cards run out
            possible_nb_of_rounds = len(self.game_pile.cards) // len(self.players)
            nb_rounds = possible_nb_of_rounds

        self.ui.render_pile(self.game_pile)
        self.ui.render_pile(self.discard_pile)

        for round_nb in range(nb_rounds):
            self.ui.render_msg(f"\nRound {round_nb + 1}:")
            more_players_than_cards_left = len(self.players) > len(self.game_pile.cards)

            if self.game_pile.is_empty():
                logging.info("No more cards left to pick from -> reshuffling")
                self.card_actions.reshuffle()

            elif more_players_than_cards_left:
                logging.info(
                    "Not enough cards in the pile for all players -> reshuffling"
                )
                self.card_actions.reshuffle()

            self.do_round()

        names_won = self.scoreboard.get_game_winners()
        players_won = tuple(
            p for p in self.players if p.name in names_won
        ) if names_won else None
        self.ui.render_game_winners(players_won)


if __name__ == "__main__":
    from ui import CLI

    logging.basicConfig(level=logging.WARNING)

    player1 = Player("evan")
    player2 = Player("viola")
    player3 = Player("lenka")
    scoreboard = ScoreBoard(["evan", "viola", "lenka"])
    game_pile = Pile.from_seed(seed="AKKQQQJJJJ", name="game")
    discard_pile = Pile("discard")
    cli = CLI()
    game_actions = GameActions(
        players=(player1, player2, player3),
        scoreboard=scoreboard,
    )
    card_actions = CardActions(
        players=(player1, player2, player3),
        game_pile=game_pile,
        discard_pile=discard_pile,
    )
    game = CardGame(
        players=(player1, player2, player3),
        game_pile=game_pile,
        discard_pile=discard_pile,
        ui=cli,
        scoreboard=scoreboard,
        game_actions=game_actions,
        card_actions=card_actions,
    )

    game.run(10)
