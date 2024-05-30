import sys
import random
import time


class DragonGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_alive = True

    def pause(self, pause_count):
        time.sleep(pause_count)

    def lore_primer(self):
        self.pause(1)
        print(
            "A thousand years ago, the entire dragon race under the banner of the Tyrant King Lubelgranz waged war with the rest of the world. They were all driven by one goal: domination"
        )
        self.pause(1)
        print(
            "Living up to their name as the supreme race, they were able to quickly conquer half of the world in less than a century spreading terror and destruction in their wake."
        )

    def intro_player(self):
        print(
            f"{self.player_name}. In front of you is the entrance to the ruins Alba Zorc. This is where the dragon king Lubelgranz retreated to along with his remaining dragon sentries."
        )
        self.pause(1)
        print(
            "It is your goal to deal the killing blow to Lubelgranz, once a Tyrant King to a thousand dragons now reduced to the last dragon alive."
        )
        self.pause(1)
        print(
            "This is supposedly the role of the Hero Abelion but he failed in the last moment allowing the weakened dragon king to summon dragon sentries to distract the heavily injured hero and make his escape."
        )
        self.pause(1)
        print(
            "The dragon should be hiding in the innermost chamber of the ruins obscured by its labyrinthine structure. Thread carefully as the remaining sentries are roaming the path leading to Lubelgranz and that countless traps remain hidden with enough power to kill anything that is not a dragon"
        )
        self.pause(1)
        print(
            "Avoid any and all confrontations with the sentries as well avoid triggering any traps. You only have a single opportunity and enough power for a single strike to kill Lubelgranz. Failure to do so will render this opportunity void, further prolonging this damned war."
        )
        self.pause(1)
        print(f"With all that said. Godspeed {self.player_name}")

    def mechanics(self):
        self.pause(1)
        print(
            "The mechanics for this game is simple. You will be asked which path to take, left or right. Either which leads to one of the two results, passing through safely or getting killed. To beat the game, you must pass through all the stages without losing your life. In doing so, you will be able to reach the final boss and dealing the killing blow to fulfill your task. The number of stages will be randomly determined between 4 and 12 at the start of the game"
        )

    def askplayer_mechanics(self):
        while True:
            print("Do you wish to read the introduction and game mechanics: \n")
            print("[1] Read both introduction and game mechanics\n")
            print("[2] Skip to the mechanics\n")
            print("[3] Skip both and head to the game\n")

            try:
                user_choice = int(input("Input the number of your choice [1-3]: "))
                if user_choice in (1, 2, 3):
                    break
                else:
                    print("Input might be outside the provided choices. Try again")
            except ValueError:
                print("Invalid input. Try again")
                continue

        match user_choice:
            case 1:
                self.intro_player()
                self.mechanics()

            case 2:
                self.mechanics()

            case 3:
                print("Understood. Will begin the game shortly")
                self.pause(1)

            case _:
                print("Fatal Error occurred. Ending application.")
                sys.exit(0)

    def determine_stages(self):
        print(
            "You took out a strange artifact provided by the Mages' Tower. It looked hastily-made but potent magics emanate from it. You activated the artifact as instructed and you suddenly felt tension from the artifact as if something or someONE is pulling you from within the ruins."
        )
        randomize_stage = random.randint(4, 12)
        self.pause(2)
        print("For debugging purposes.", randomize_stage)
        if randomize_stage < 6:
            print(
                "The tension felt quite light. If the instructions were to be trusted, Lubelgranz's location is nearby. With this knowledge in hand you proceed with the mission by entering the ruins."
            )
        elif 6 <= randomize_stage <= 8:
            print(
                "You feel a strong pull from within as you held the artifact but it was not strong enough to shift your balance. This must mean Lubelgranz is hiding somewhere in the middle of the labyrinth."
            )
            print(
                "You proceed to enter the ruin with great caution and set off to carry out this mission"
            )
        else:
            print(
                "You feel a very strong pull coming from deep within the ruins. It is clear Lubelgranz is located at the innermost chamber of the labyrinth and is now made aware of your presence.\n"
            )
            print(
                "Despite that you must carry out the mission so you stepped inside of the ruin to put an end to this war once and for all."
            )


def play_game(get_player):
    game_instance = DragonGame(get_player)
    game_instance.pause(0.5)
    game_instance.askplayer_mechanics()
    game_instance.determine_stages()


if __name__ == "__main__":
    get_player = input("Tell us your name before you start this game: ")
    play_game(get_player)
