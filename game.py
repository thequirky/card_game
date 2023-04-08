from card import Pile
from player import Player
from scoreboard import ScoreBoard
from ui import UI


class CardGame:

    def __init__(self,
                 player: Player,
                 other_player: Player,
                 pile: Pile,
                 discard_pile: Pile,
                 ui: UI,
                 scoreboard: ScoreBoard) -> None:
        self.pile = pile
        self.discard_pile = discard_pile
        self.player = player
        self.other_player = other_player
        self.ui = ui
        self.scoreboard = scoreboard

    @property
    def players(self) -> tuple[Player, Player]:
        return self.player, self.other_player

    def all_players_pick_cards(self) -> None:
        for player in self.players:
            top_card = self.pile.get_top_card()
            if not top_card:
                self.ui.render_msg(f"{player.name} could not pick a card...")
            player.picks_up_card(card=top_card)

    def all_players_put_down_cards(self) -> None:
        for player in self.players:
            card = player.puts_down_card()
            self.discard_pile.add_card_to_top(card=card)

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

    def update_scoreboard(self) -> None:
        if self.round_winner:
            board = self.scoreboard
            board.increase_player_score_by(player_name=self.round_winner.name,
                                           value=self.round_winner.card.value)
            board.increment_player_rounds_won(player_name=self.round_winner.name)

    def more_players_than_cards(self) -> bool:
        return len(self.players) > len(self.pile.cards)

    def play_round(self) -> None:
        self.pile.shuffle_cards()
        self.ui.render_pile(pile=self.pile)
        self.all_players_pick_cards()
        self.update_scoreboard()
        self.ui.render_player_cards(players=self.players)
        self.ui.render_round_winner(player=self.round_winner)
        self.all_players_put_down_cards()
        self.ui.render_pile(pile=self.pile)
        self.ui.render_pile(pile=self.discard_pile)
        self.ui.render_scoreboard(self.scoreboard)

    def run(self, nb_rounds: int = 1) -> None:
        self.ui.render_pile(pile=self.pile)
        for nb_of_round in range(nb_rounds):
            self.ui.render_msg(f"\nRound {nb_of_round + 1}:")
            if self.pile.is_empty():
                self.ui.render_msg(msg="No more cards left to pick from...")
                break
            if self.more_players_than_cards():
                self.ui.render_msg(msg="Not enough cards left in the pile for all players...")
                break
            self.play_round()
        self.ui.render_game_winner(player=self.game_winner)
        self.scoreboard.reset_rounds()
        self.scoreboard.reset_scores()


if __name__ == "__main__":
    from ui import CLI

    evan = Player(name="Evan")
    viola = Player(name="Viola")
    scoreboard = ScoreBoard()
    scoreboard.register_player(player_name=evan.name)
    scoreboard.register_player(player_name=viola.name)
    pile = Pile.from_str(seed_str="AKKQQQ", name="game pile")
    discard_pile = Pile(name="discard pile")
    cli = CLI()
    nb_rounds = 3
    game = CardGame(player=viola,
                    other_player=evan,
                    pile=pile,
                    discard_pile=discard_pile,
                    ui=cli,
                    scoreboard=scoreboard)

    game.run(nb_rounds=nb_rounds)
