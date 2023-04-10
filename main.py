from config import CONFIG1, CONFIG2, game_factory


def main():
    # game1 = game_factory(from_dict=CONFIG1)
    # game1.run(nb_rounds=3)

    game2 = game_factory(from_dict=CONFIG2)
    game2.run(nb_rounds=0)  # 0: keep doing turns until cards run out


if __name__ == "__main__":
    main()
