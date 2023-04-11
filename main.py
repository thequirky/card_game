from config import CONFIG
from factory import game_factory
import logging


def main():
    logging.basicConfig(level=logging.ERROR)

    game = game_factory(config_dct=CONFIG)
    game.run()

    # or can do multiple runs:
    # game.run(nb_rounds=3)
    # game.run()  # continues previous run

if __name__ == "__main__":
    main()
