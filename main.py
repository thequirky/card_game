from config import GameConfig


def main():
    config = GameConfig(names=["Evan", "Viola"], pile_str="AKKQQQJJJJ")
    game = config.game
    game.run(nb_rounds=5)


if __name__ == "__main__":
    main()
