from card import Pile


pile = Pile.from_seed(seed="AAAKKKQQQ", name="test")
pile.shuffle()

print(pile)

def hide(pile:Pile) -> None:
    new = list(range(1, len(pile.cards)+1))
    return new

h = hide(pile)
nb = input("pick no ->")
nb = int(nb)-1

picked = pile.cards[nb].name

h[nb] = picked

print(h)
