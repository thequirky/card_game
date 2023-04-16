from factory import game_factory
import logging


CONFIG1 = {"names": ["evan", "viola"], "seed": "AKKQQQJJJJ"}
CONFIG2 = {"names": ["evan", "viola", "olivia", "lenka"], "seed": "AAAAKKKKQQQQJJJJ"}


def main():
    logging.basicConfig(level=logging.ERROR)

    game = game_factory(CONFIG1)
    game.run()


if __name__ == "__main__":
    main()
