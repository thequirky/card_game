from config import CONFIG
from factory import game_factory
import logging


def main():
    logging.basicConfig(level=logging.ERROR)

    game = game_factory(config=CONFIG)
    game.run()


if __name__ == "__main__":
    main()
