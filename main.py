import logging

from config import Config


def main():
    logging.basicConfig(level=logging.INFO)

    config1 = Config(names=["evan", "viola"], seed="AKKQQQJJJJ")
    config2 = Config(names=["evan", "viola", "lenka"], seed="AAKKKQQQQJJJJ")
    config3 = Config(names=["evan", "viola", "olivia", "lenka"], seed="AAAAKKKKQQQQJJJJ")

    game = config1.game
    game.run()


if __name__ == "__main__":
    main()
