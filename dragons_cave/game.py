import random
import time


class dragonGame:
    def randomize(self) -> int:
        randomized_stages = random.randint(4, 12)
        return randomized_stages


def disPlayIntro():
    print(
        "Before you is the entrance to the Albatraz Dungeon where the last dragon, Lubelgranz retreated."
    )
    time.sleep(3)
    print(
        "You are to carefully proceed through the labyrinthine dungeon avoiding Lubelgranz's clone sentries till you reach him and deal the killing blow"
    )
    time.sleep(3)


def makeChoice():
    paths = random.randint(2, 3)


def game():
    draGame = dragonGame()
    disPlayIntro()
    stages = draGame.randomize(draGame)
