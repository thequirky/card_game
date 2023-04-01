from card import CARD_VALUE
from deck import Deck
from player import Player


class CardGame:

    def __init__(self, player, other_player, deck, ui):
        self.deck = deck
        self.player = player
        self.other_player = other_player
        self.ui = ui

    @property
    def players(self) -> tuple[Player, Player]:
        return self.player, self.other_player

    def pick_cards_for_players(self) -> None:
        for player in self.players:
            top_card = self.deck.pick_card_from_top_of_pile()
            player.pick_up_card(top_card)
            player.increase_score_by(value=CARD_VALUE[top_card])

    def players_put_down_cards(self) -> None:
        for player in self.players:
            card = player.put_down_card()
            self.deck.add_card_to_top_of_pile(card)

    def reset_scores(self) -> None:
        for player in self.players:
            player.reset_score()

    @property
    def winner(self) -> Player:
        if self.player.score == self.other_player.score:
            return None
        elif self.player.score > self.other_player.score:
            return self.player
        else:
            return self.other_player

    @property
    def round_winner(self) -> Player:
        if CARD_VALUE[self.player.card_held] == CARD_VALUE[self.other_player.card_held]:
            return None
        elif CARD_VALUE[self.player.card_held] > CARD_VALUE[self.other_player.card_held]:
            return self.player
        else:
            return self.other_player

    def play_round(self) -> None:
        if not self.deck:
            # no more cards to pick from deck
            return
        self.pick_cards_for_players()
        for player in self.players:
            self.ui.show_player_card(player=player)
        self.ui.show_round_winner(player=self.round_winner)
        self.players_put_down_cards()
        self.ui.show_cards_pile(deck=self.deck)
        self.ui.show_removed_cards_pile(deck=self.deck)
        self.ui.show_scoreboard(player=self.player, other_player=self.other_player)

    def run(self, nb_rounds) -> None:
        for _ in range(nb_rounds):
            self.play_round()
        self.ui.show_game_winner(player=self.winner)
        self.reset_scores()


if __name__ == "__main__":
    from ui import CLI

    evan = Player(name="Evan")
    viola = Player(name="Viola")
    deck = Deck.from_str(card_string="akkkkqqqq", shuffle=True)
    cli = CLI()
    nb_rounds = 3
    cli.show_cards_pile(deck=deck, separator=True)
    game = CardGame(player=viola, other_player=evan, deck=deck, ui=cli)

    game.run(nb_rounds=nb_rounds)
