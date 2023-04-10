from config import CONFIG1, CONFIG2, config_game


def main():
    # game1 = config_game(CONFIG1)
    # game1.run(nb_rounds=3)
    
    game2 = config_game(CONFIG2)
    game2.run(nb_rounds=0)  # 0: keep doing turns until cards run out


if __name__ == "__main__":
    main()
