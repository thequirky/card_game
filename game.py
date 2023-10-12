import logging

from card import Pile
from player import Player
from scoreboard import ScoreBoard
from ui import UI


def deal_random(players: tuple[Player], game_pile: Pile) -> None:
    for player in players:
        drawn_card = game_pile.draw_random()
        player.hold(drawn_card)

def discard_all(players: tuple[Player], discard_pile: Pile) -> None:
    for player in players:
        discarded = player.discard()
        discard_pile.add(discarded)

def reshuffle(game_pile: Pile, discard_pile: Pile) -> None:
    game_pile.reshuffle(discard_pile)
    discard_pile.cards = []

def get_round_winners(players: tuple[Player]) -> tuple[Player]:
    max_value = max(player.hand.value for player in players)
    return tuple(player for player in players if player.hand.value == max_value)

def update_scoreboard(scoreboard: ScoreBoard, players: tuple[Player]) -> None:
    for winner in get_round_winners(players):
        scoreboard.actions.increment_score_of(name=winner.name, value=winner.hand.value)
        scoreboard.actions.increment_rounds_of(winner.name)


class CardGame:
    def __init__(self, players: tuple[Player], game_pile: Pile, ui: UI, scoreboard: ScoreBoard) -> None:
        self.game_pile = game_pile
        self.players = players
        self.ui = ui
        self.scoreboard = scoreboard
        self.discard_pile = Pile("discard")

    def do_round(self) -> None:
        self.game_pile.shuffle()
        self.ui.render_pile(self.game_pile)
        deal_random(self.players, self.game_pile)
        update_scoreboard(self.scoreboard, self.players)
        self.ui.render_hands(self.players)
        self.ui.render_round_winner(get_round_winners(self.players))
        discard_all(self.players, self.discard_pile)
        # self.ui.render_pile(self.game_pile)
        # self.ui.render_pile(self.discard_pile)
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
                reshuffle(self.game_pile, self.discard_pile)

            elif more_players_than_cards_left:
                logging.info("Not enough cards in the pile for all players -> reshuffling")
                reshuffle(self.game_pile, self.discard_pile)

            self.do_round()

        names_won = self.scoreboard.actions.get_game_winners()
        players_won = tuple(p for p in self.players if p.name in names_won)
        self.ui.render_game_winners(players_won)


if __name__ == "__main__":
    from ui import CLI
    from factory import deduplicate

    logging.basicConfig(level=logging.WARNING)

    names = ("viola", "evan", "lenka")
    names = deduplicate(names)
    players = Player.from_names(names)
    scoreboard = ScoreBoard.from_players(players)
    game_pile = Pile.from_seed(seed="AKKQQQJJJJ", name="game")
    ui = CLI()
    game = CardGame(
        players=players,
        game_pile=game_pile,
        ui=ui,
        scoreboard=scoreboard,
    )

    game.run(10)
