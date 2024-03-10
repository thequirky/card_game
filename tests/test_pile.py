import unittest

from card.card import Card
from card.pile import Pile


class TestPileMethods(unittest.TestCase):
    def test_init_name(self):
        p = Pile("game")
        self.assertEqual(p.name, "Game")

    def test_create_from_seed(self):
        p = Pile.from_seed(seed="AAKKQQ", name="from seed")
        self.assertEqual(p.cards[0], Card.Ace)

    def test_shuffle_pile(self):
        p1 = Pile.from_seed(seed="AKKKKQQQQJJJJ", name="pile 1")
        p2 = Pile.from_seed(seed="AKKKKQQQQJJJJ", name="pile 2")
        p2.shuffle()
        self.assertNotEqual(p1.cards[0], p2.cards[0])

    def test_get_top_card(self):
        p = Pile.from_seed(seed="KKKA", name="pile")
        c = p.draw_top()
        self.assertEqual(c, Card.Ace)

    def test_add_to_top(self):
        p = Pile.from_seed(seed="KKKK", name="pile")
        p.add(Card.Ace)
        self.assertEqual(p.cards[-1], Card.Ace)


if __name__ == "__main__":
    unittest.main()
