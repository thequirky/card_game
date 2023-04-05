from card import Pile
from player import Player
from ui import UI


class CardGame:

    # todo: make game winner win based on nb of rounds won
    # todo: add another game in which winner wins based on scores

    def __init__(self, player: Player, other_player: Player, pile: Pile, discard_pile: Pile, ui: UI):
        self.pile = pile
        self.discard_pile = discard_pile
        self.player = player
        self.other_player = other_player
        self.ui = ui

    @property
    def players(self) -> tuple[Player, Player]:
        return self.player, self.other_player

    def pick_cards_for_players(self) -> None:
        for player in self.players:
            top_card = self.pile.get_top_card()
            if not top_card:
                self.ui.render_msg(f"{player.name} could not pick a card...")
            player.pick_up_card(card=top_card)
            player.increase_score_by(value=top_card.value)

    def players_put_down_cards(self) -> None:
        for player in self.players:
            card = player.put_down_card()
            self.discard_pile.add_cards_to_top(cards_to_add=card)

    def reset_scores(self) -> None:
        for player in self.players:
            player.reset_score()

    @property
    def game_winner(self) -> Player | None:
        if self.player.score == self.other_player.score:
            return None  # tie
        elif self.player.score > self.other_player.score:
            return self.player
        else:
            return self.other_player

    @property
    def round_winner(self) -> Player | None:
        if self.player.card.value == self.other_player.card.value:
            return None  # tie
        elif self.player.card.value > self.other_player.card.value:
            return self.player
        else:
            return self.other_player

    def play_round(self) -> None:
        self.pile.shuffle_cards()
        self.ui.render_pile(pile=self.pile)
        self.pick_cards_for_players()
        self.ui.render_player_cards(players=self.players)
        self.ui.render_round_winner(player=self.round_winner)
        self.players_put_down_cards()
        self.ui.render_pile(pile=self.pile)
        self.ui.render_pile(pile=self.discard_pile)
        self.ui.render_scoreboard(player=self.player, other_player=self.other_player)

    def run(self, nb_rounds: int = 1) -> None:
        self.ui.render_pile(pile=self.pile)
        for idx, _ in enumerate(range(nb_rounds)):
            self.ui.render_msg(f"\nRound {idx + 1}:")
            if not self.pile.cards:
                self.ui.render_msg(msg="No more cards left to pick from...")
                break
            if len(self.pile.cards) < len(self.players):
                self.ui.render_msg(msg="Not enough cards left to pick from...")
                break
            self.play_round()
        self.ui.render_game_winner(player=self.game_winner)
        self.reset_scores()


if __name__ == "__main__":
    from ui import CLI

    evan = Player(name="Evan")
    viola = Player(name="Viola")
    pile = Pile.from_str(seed_str="AKKQQQ", name="game pile")
    discard_pile = Pile(name="discard pile")
    cli = CLI()
    nb_rounds = 3
    game = CardGame(player=viola, other_player=evan, pile=pile, discard_pile=discard_pile, ui=cli)

    game.run(nb_rounds=nb_rounds)
