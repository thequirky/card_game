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

    @property
    def _more_players_than_cards(self) -> bool:
        return len(self.players) > len(self.game_pile.cards)

    def get_game_winners(self) -> list[Player] | None:
        names_won = self.scoreboard.get_score_leaders()
        players_won = [
            p for p in self.players if p.name in names_won
        ]
        if len(players_won) > 1:
            players_won = self.resolve_tie(players_won)
        return players_won

    def resolve_tie(self, players: list[Player]) -> list[Player] | None:
        player_to_rounds = {p: self.scoreboard.get_rounds_of(p.name) for p in players if p.name}
        max_rounds = max(player_to_rounds.values())
        players_won = [
            p for p in player_to_rounds if self.scoreboard.get_rounds_of(p.name) == max_rounds
        ]
        if len(players_won) > 1 and len(self.players) == 2:  # still tie
            return None
        return players_won

    @property
    def _player_to_card_value(self) -> dict[Player, int]:
        return {p: p.hand.value for p in self.players}

    def get_round_winners(self) -> list[Player] | None:
        unique_values = self._player_to_card_value.values()
        if len(unique_values) == 1:  # means all players hold same card -> tie
            return None
        max_value = max(unique_values)
        players_with_max_value  = [
            p for p in self.players if p.hand.value == max_value
        ]
        return players_with_max_value

    def players_pick_cards(self) -> None:
        for player in self.players:
            picked_card = self.game_pile.get_random_card()
            player.hold(picked_card)

    def players_discard_cards(self) -> None:
        for player in self.players:
            discarded = player.discard()
            self.discard_pile.add_to_top(discarded)

    def update_scoreboard(self) -> None:
        winners = self.get_round_winners()
        if not winners:
            return
        sb = self.scoreboard
        for winner in winners:
            sb.increment_score(
                name=winner.name,
                value=winner.hand.value,
            )
            sb.increment_rounds_won(winner.name)

    def do_turn(self) -> None:
        self.game_pile.shuffle()
        self.ui.render_pile(self.game_pile)
        self.players_pick_cards()
        self.update_scoreboard()
        self.ui.render_player_cards(self.players)
        self.ui.render_turn_winner(self.get_round_winners())
        self.players_discard_cards()
        self.ui.render_pile(self.game_pile)
        self.ui.render_pile(self.discard_pile)
        self.ui.render_scoreboard(str(self.scoreboard))

    def run(self, nb_rounds: int | None = None) -> None:
        if not nb_rounds:  # keep doing turns until cards run out
            nb_rounds = len(self.game_pile.cards) // len(self.players)
        self.ui.render_pile(self.game_pile)
        for nb_of_round in range(nb_rounds):
            self.ui.render_msg(f"\nRound {nb_of_round + 1}:")
            if self.game_pile.is_empty:
                logging.info("No more cards left to pick from.")
                break
            if self._more_players_than_cards:
                logging.info("Not enough cards in the pile for all players.")
                break
            self.do_turn()
        self.ui.render_game_winner(self.get_game_winners())
        self.scoreboard.reset_rounds()
        self.scoreboard.reset_scores()


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

    game.run()
