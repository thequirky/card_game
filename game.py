from card import CARD_VALUE, Pile
from player import Player
from ui import UI


class CardGame:

    def __init__(self, player: Player, other_player: Player, pile: Pile, removed_cards_pile: Pile, ui: UI):
        self.pile = pile
        self.removed_cards_pile = removed_cards_pile
        self.player = player
        self.other_player = other_player
        self.ui = ui

    @property
    def players(self) -> tuple[Player, Player]:
        return self.player, self.other_player

    def pick_cards_for_players(self) -> None:
        for player in self.players:
            top_card = self.pile.get_top_card()
            player.pick_up_card(top_card)
            player.increase_score_by(value=CARD_VALUE[top_card])

    def players_put_down_cards(self) -> None:
        for player in self.players:
            card = player.put_down_card()
            self.removed_cards_pile.add_cards_to_top(new_cards=card)

    def reset_scores(self) -> None:
        for player in self.players:
            player.reset_score()

    @property
    def game_winner(self) -> Player:
        score_of_player = self.player.get_score()
        score_of_other_player = self.other_player.get_score()
        if score_of_player == score_of_other_player:
            return None  # tie
        elif score_of_player > score_of_other_player:
            return self.player
        else:
            return self.other_player

    @property
    def round_winner(self) -> Player:
        card_value_of_player = CARD_VALUE[self.player.get_held_card()]
        card_valuer_of_other_player = CARD_VALUE[self.other_player.get_held_card()]
        if card_value_of_player == card_valuer_of_other_player:
            return None  # tie
        elif card_value_of_player > card_valuer_of_other_player:
            return self.player
        else:
            return self.other_player

    def play_round(self) -> None:
        if not self.pile:
            print("no more cards to pick from deck")  # TODO: add to CLI
            return
        self.pile.shuffle_cards()
        self.ui.show_pile(pile=self.pile, pile_type="main")
        self.pick_cards_for_players()
        for player in self.players:
            self.ui.show_player_card(player=player)
        self.ui.show_round_winner(player=self.round_winner)
        self.players_put_down_cards()
        self.ui.show_pile(pile=self.removed_cards_pile, pile_type="removed cards")
        self.ui.show_scoreboard(player=self.player, other_player=self.other_player)

    def run(self, nb_rounds: int = 1) -> None:
        for _ in range(nb_rounds):
            self.play_round()
        self.ui.show_game_winner(player=self.game_winner)
        self.reset_scores()


if __name__ == "__main__":
    from ui import CLI, UI

    evan = Player(name="Evan")
    viola = Player(name="Viola")
    pile = Pile.from_str(pile_str="AKKQQQ")
    removed_pile = Pile()
    cli = CLI()
    nb_rounds = 3
    cli.show_pile(pile=pile, pile_type="start", separator=True)
    game = CardGame(player=viola, other_player=evan, pile=pile, removed_cards_pile=removed_pile, ui=cli)

    game.run(nb_rounds=nb_rounds)
