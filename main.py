from config import CONFIG1
from factory import game_factory
import logging


def main():
    logging.basicConfig(level=logging.ERROR)

    game = game_factory(config=CONFIG1)
    game.run()


if __name__ == "__main__":
    main()
