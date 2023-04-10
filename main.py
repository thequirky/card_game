from config import config_game


def main():
    game = config_game(name1="evan", name2="viola", pile_str="AKKQQQJJJJ")
    game.run(nb_rounds=5)


if __name__ == "__main__":
    main()
