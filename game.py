from card import Pile
from player import Player
from scoreboard import ScoreBoard
from ui import UI
import logging


class CardGame:
    def __init__(
        self,
        player: Player,
        other_player: Player,
        game_pile: Pile,
        discard_pile: Pile,
        ui: UI,
        scoreboard: ScoreBoard,
    ) -> None:
        self.game_pile = game_pile
        self.discard_pile = discard_pile
        self.player = player
        self.other_player = other_player
        self.ui = ui
        self.scoreboard = scoreboard

    @property
    def players(self) -> tuple[Player, Player]:
        return self.player, self.other_player

    @property
    def more_players_than_cards(self) -> bool:
        return len(self.players) > len(self.game_pile.cards)

    @property
    def game_winner(self) -> Player | None:
        s1 = self.scoreboard.get_score_of(self.player.name)
        s2 = self.scoreboard.get_score_of(self.other_player.name)
        if s1 == s2:
            return None  # tie
        elif s1 > s2:
            return self.player
        else:
            return self.other_player

    @property
    def round_winner(self) -> Player | None:
        cv1 = self.player.card.value
        cv2 = self.other_player.card.value
        if cv1 == cv2:
            return None  # tie
        elif cv1 > cv2:
            return self.player
        else:
            return self.other_player

    def players_picking_cards(self) -> None:
        for player in self.players:
            picked_card = self.game_pile.get_random_card()
            player.hold(picked_card)

    def players_discarding_cards(self) -> None:
        for player in self.players:
            card = player.discard()
            self.discard_pile.add_to_top(card)

    def update_scoreboard(self) -> None:
        if self.round_winner:
            sb = self.scoreboard
            sb.increase_player_score_by(
                player_name=self.round_winner.name,
                value=self.round_winner.card.value,
            )
            sb.increment_player_rounds_won(self.round_winner.name)

    def do_turn(self) -> None:
        self.game_pile.shuffle_cards()
        self.ui.render_pile(self.game_pile)
        self.players_picking_cards()
        self.update_scoreboard()
        self.ui.render_player_cards(self.players)
        self.ui.render_round_winner(self.round_winner)
        self.players_discarding_cards()
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
        self.ui.render_game_winner(self.game_winner)
        self.scoreboard.reset_rounds()
        self.scoreboard.reset_scores()


if __name__ == "__main__":
    from ui import CLI

    logging.basicConfig(level=logging.INFO)

    player1 = Player("evan")
    player2 = Player("viola")
    scoreboard = ScoreBoard()
    scoreboard.register(player1.name)
    scoreboard.register(player2.name)
    game_pile = Pile.from_str(seed_str="AKKQQQJJJJ", name="game")
    discard_pile = Pile("discard")
    cli = CLI()
    game = CardGame(
        player=player1,
        other_player=player2,
        game_pile=game_pile,
        discard_pile=discard_pile,
        ui=cli,
        scoreboard=scoreboard,
    )

    game.run()
