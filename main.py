from config import CONFIG1, CONFIG2
from factory import game_factory
import logging


def main():
    logging.basicConfig(level=logging.ERROR)

    # game1 = game_factory(config_dct=CONFIG1)
    # game1.run(nb_rounds=3)

    game2 = game_factory(config_dct=CONFIG2)
    game2.run()


if __name__ == "__main__":
    main()
