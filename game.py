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
    def more_players_than_cards(self) -> bool:
        return len(self.players) > len(self.game_pile.cards)

    @property
    def game_winners(self) -> list[Player] | None:
        player_to_score = {
            p: self.scoreboard.get_score_of(p.name) for p in self.players
        }
        max_score = max(self.scoreboard.scores.values())
        winners = [
            p for p in player_to_score.keys() if player_to_score[p] == max_score
        ]
        return winners

    @property
    def turn_winners(self) -> list[Player] | None:
        player_to_card_value: dict[Player, int] = {
            player: player.card.value for player in self.players
        }
        nb_unique_values = len(set(player_to_card_value.values()))
        if nb_unique_values == 1:
            return None  # tie
        max_value = max(player_to_card_value.values())
        players_with_max_value  = [
            p for p in self.players if p.card.value == max_value
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
        if not self.turn_winners:
            return
        sb = self.scoreboard
        for winner in self.turn_winners:
            sb.increment_score(
                name=winner.name,
                value=winner.card.value,
            )
            sb.increment_rounds_won(winner.name)

    def do_turn(self) -> None:
        self.game_pile.shuffle()
        self.ui.render_pile(self.game_pile)
        self.players_pick_cards()
        self.update_scoreboard()
        self.ui.render_player_cards(self.players)
        self.ui.render_turn_winner(self.turn_winners)
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
                logging.warning("No more cards left to pick from.")
                break
            if self.more_players_than_cards:
                logging.warning("Not enough cards in the pile for all players.")
                break
            self.do_turn()
        self.ui.render_game_winner(self.game_winners)
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
