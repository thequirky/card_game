from config import CONFIG1, CONFIG2, game_factory
import logging


def main():
    logging.basicConfig(level=logging.ERROR)

    # game1 = game_factory(from_dict=CONFIG1)
    # game1.run(nb_rounds=3)

    game2 = game_factory(from_dict=CONFIG2)
    game2.run(nb_rounds=11)  # 0: keep doing turns until cards run out


if __name__ == "__main__":
    main()
