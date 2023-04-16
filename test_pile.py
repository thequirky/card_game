import unittest

from card import Card, Pile


class TestPileMethods(unittest.TestCase):
    def test_init_name(self):
        p = Pile("game")
        self.assertEqual(p.name, "game")

    def test_empty_equality(self):
        p = Pile("game")
        d = Pile("discard")
        self.assertEqual(p, d)

    def test_create_from_seed(self):
        p = Pile.from_seed(seed="AAKKQQ", name="from seed")
        self.assertEqual(p.cards[0], Card.Ace)

    def test_equality_pile(self):
        p1 = Pile.from_seed(seed="AAKKQQ", name="pile 1")
        p2 = Pile.from_seed(seed="AAKKQQ", name="pile 2")
        self.assertEqual(p1, p2)

    def test_shuffled_equality_pile(self):
        p1 = Pile.from_seed(seed="AKKKKQQQQJJJJ", name="pile 1")
        p2 = Pile.from_seed(seed="AKKKKQQQQJJJJ", name="pile 2")
        p2.shuffle()
        self.assertNotEqual(p1, p2)

    def test_shuffle_pile(self):
        p1 = Pile.from_seed(seed="AKKKKQQQQJJJJ", name="pile 1")
        p2 = Pile.from_seed(seed="AKKKKQQQQJJJJ", name="pile 2")
        p2.shuffle()
        self.assertNotEqual(p1.cards[0], p2.cards[0])

    def test_get_top_card(self):
        p = Pile.from_seed(seed="KKKA", name="pile")
        c = p.get_top_card()
        self.assertEqual(c, Card.Ace)

    def test_add_to_top(self):
        p = Pile.from_seed(seed="KKKK", name="pile")
        p.add_to_top(Card.Ace)
        self.assertEqual(p.cards[-1], Card.Ace)


if __name__ == "__main__":
    unittest.main()
