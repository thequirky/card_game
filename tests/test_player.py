import unittest

from card import Card
from player import Player


class TestPlayerMethods(unittest.TestCase):

    def test_capitalise_name(self):
        p = Player("evan")
        self.assertEqual(p.name, "Evan")

    def test_initialises_with_no_card(self):
        p = Player("evan")
        self.assertIsNone(p.card)

    def test_hold_card(self):
        p = Player("evan")
        p.hold(Card.Ace)
        self.assertEqual(p.card, Card.Ace)

    def test_holding(self):
        p = Player("evan")
        p.hold(Card.Ace)
        self.assertTrue(p.holding)

    def test_hold_while_already_holding(self):
        p = Player("evan")
        p.hold(Card.Ace)
        with self.assertRaises(Exception):
            p.hold(Card.Joker)

    def test_discard(self):
        p = Player("evan")
        p.hold(Card.Ace)
        p.discard()
        self.assertFalse(p.holding)

    def test_discard_with_no_card(self):
        p = Player("evan")
        p.hold(Card.Ace)
        p.discard()
        with self.assertRaises(Exception):
            p.discard()


if __name__ == '__main__':
    unittest.main()
