from factory import game_factory
import logging


NB_ROUNDS = 0
# NB_ROUNDS = 10

CONFIG = {"names": ("evan", "viola"), "seed": "AKKQQQJJJJ"}
# CONFIG = {"names": ("evan", "viola", "lenka"), "seed": "AAKKKQQQQJJJJ"}
# CONFIG = {"names": ("evan", "viola", "olivia", "lenka"), "seed": "AAAAKKKKQQQQJJJJ"}


def main():
    logging.basicConfig(level=logging.ERROR)

    game = game_factory(CONFIG)
    game.run(NB_ROUNDS)


if __name__ == "__main__":
    main()
