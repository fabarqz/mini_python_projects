import random
import time


class dragonGame:
    def randomize(self) -> int:
        randomized_stages = random.randint(4, 12)
        return randomized_stages

    def dragonAction(self):
        defeat_scenes = [
            "Alas! You were caught by a sentry delivering a swift slash splitting your body into two",
            "You died! A sentry hiding in the dark out of your sight struck you in the back piercing through your heart with its spear-like tail",
            "The moment you step into the chamber the dark interior suddenly got bright as a ball of fire flies towards you. You were unable to dodge thus got incinerated to ashes",
            "Alas you were killed by a ceiling made of spikes fall on top you",
            "Alas before you could get inside the chamber, a dragon sentry pops out of the dark with it maws wide open devouring you",
        ]

        random_scene = random.choice(defeat_scenes)

        return random_scene


def disPlayIntro():
    print(
        "Before you is the entrance to the Albatraz Dungeon where the last dragon, Lubelgranz retreated."
    )
    time.sleep(2)
    print(
        "You are to carefully proceed through the labyrinthine dungeon avoiding Lubelgranz's clone sentries till you reach him and deal the killing blow"
    )
    time.sleep(2)


def makeChoice():
    print(
        "The path before you splits into two. Both chambers are shrouded in darkness but what is certain is that one will lead you close to the dragon while the other your doom."
    )
    time.sleep(2)

    while True:
        try:
            userChoice = input("Which chamber will you enter, the left or the right?")
            if userChoice != "left" and userChoice != "right":
                raise ValueError("That is an invalid choice")

            return userChoice
        except ValueError as e:
            print(f"Error. {e}. Try again")


def decideResult(choice):
    time.sleep(2)
    decision = random.randint(1, 2)
    if decision == 2:
        print(
            f"You took the {choice} chamber. It appears that no sentry is patrolling this area allowing you to venture closer to  the target"
        )
        return True
    else:
        defeat = dragonGame.dragonAction(dragonGame)
        print(f"You took the {choice} chamber.{defeat}")
        return False


def gameLoop(stages):
    alive = True
    i = 0
    while i < stages - 1 and alive == True:
        getChoice = makeChoice()
        getResult = decideResult(getChoice)
        alive = getResult
        i += 1
    time.sleep(2)
    print(
        "You traversed through numerous chambers and managed to evade Lubelgranz's sentries. At this meoment you arrived ath the dungeon's final chamber where the last dragon is hiding."
    )
    time.sleep(2)
    print(
        "Lubelgranz, once the mighty tyrant that commanded his dragonkin to terrorize and enslave the rest of humanity, is now reduced to a pathetic sight the moment it saw you enter the room"
    )
    time.sleep(2)
    print(
        "It was powerless. The summoning of sentries took all of its remaining powers and has no way of recalling them to its aid."
    )
    time.sleep(2)
    print(
        "It tries to open its mouth perhaps to make a plea. But before a sound could escape its maw you unleashed your trump card with all the rage in your heart to put an end to this once and for all"
    )
    time.sleep(2)
    print(
        "It was a single downward slash driven by unmeasurable force that bisects not only the dragon in half but also the remaining section of the dungeon behind it."
    )


def game():
    draGame = dragonGame()
    disPlayIntro()
    stages = draGame.randomize()
    print(stages)
    gameLoop(stages)


game()
