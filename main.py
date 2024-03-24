import logging

from game import CardGame


def main():
    logging.basicConfig(level=logging.INFO)

    game = CardGame.from_config(names=["evan", "viola"], seed="AKKQQQJJJJ")
    # game = CardGame.from_config(names=["evan", "viola", "lenka"], seed="AAKKKQQQQJJJJ")
    # game = CardGame.from_config(names=["evan", "viola", "olivia", "lenka"], seed="AAAAKKKKQQQQJJJJ")

    game.run()


if __name__ == "__main__":
    main()
