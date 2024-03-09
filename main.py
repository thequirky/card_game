import logging

from config import Config


def main():
    logging.basicConfig(level=logging.INFO)

    config = Config(names=["evan", "viola"], seed="AKKQQQJJJJ")
    # config = Config(names=["evan", "viola", "lenka"], seed="AAKKKQQQQJJJJ")
    # config = Config(names=["evan", "viola", "olivia", "lenka"], seed="AAAAKKKKQQQQJJJJ")

    game = config.game
    game.run()


if __name__ == "__main__":
    main()
