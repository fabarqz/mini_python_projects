import sys
import random
import time


class DragonGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_alive = True

    def lore_primer(self):
        time.sleep(1)
        print(
            "A thousand years ago, the entire dragon race under the banner of the Tyrant King Lubelgranz waged war with the rest of the world. They were all driven by one goal: domination"
        )
        time.sleep(1)
        print(
            "Living up to their name as the supreme race, they were able to quickly conquer half of the world in less than a century spreading terror and destruction in their wake."
        )

    def intro_player(self):
        print(
            f"{self.player_name}. In front of you is the entrance to the ruins Alba Zorc. This is where the dragon king Lubelgranz retreated to along with his remaining dragon sentries."
        )
        time.sleep(1)
        print(
            "It is your goal to deal the killing blow to Lubelgranz, once a Tyrant King to a thousand dragons now reduced to the last dragon alive."
        )
        time.sleep(1)
        print(
            "This is supposedly the role of the Hero Abelion but he failed in the last moment allowing the weakened dragon king to summon dragon sentries to distract the heavily injured hero and make his escape."
        )
        time.sleep(1)
        print(
            "The dragon should be hiding in the innermost chamber of the ruins obscured by its labyrinthine structure. Thread carefully as the remaining sentries are roaming the path leading to Lubelgranz and that countless traps remain hidden with enough power to kill anything that is not a dragon"
        )
        time.sleep(1)
        print(
            "Avoid any and all confrontations with the sentries as well avoid triggering any traps. You only have a single opportunity and enough power for a single strike to kill Lubelgranz. Failure to do so will render this opportunity void, further prolonging this damned war."
        )
        time.sleep(1)
        print(f"With all that said. Godspeed {self.player_name}")

    def mechanics(self):
        time.sleep(1)
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
                time.sleep(1)

            case _:
                print("Fatal Error occurred. Ending application.")
                sys.exit(0)

    def randomize_stages(self):
        randomize_stage = random.randint(4, 12)
        return randomize_stage

    def determine_stages(self, stages):
        time.sleep(1)
        print(
            "You took out a strange artifact provided by the Mages' Tower. It looked hastily-made but potent magics emanate from it. You activated the artifact as instructed and you suddenly felt tension from the artifact as if something or someONE is pulling you from within the ruins."
        )
        time.sleep(2)
        if stages < 6:
            print(
                "The tension felt quite light. If the instructions were to be trusted, Lubelgranz's location is nearby. With this knowledge in hand you proceed with the mission by entering the ruins."
            )
        elif 6 <= stages <= 8:
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

    def decide_stage(self, stages):
        i = 0
        print(
            "After walking a barely-lit hallway without any incident, the path in front of you splits in two chambers shrouded in absolute darkness."
        )
        try:
            path_choice = input(
                "So which path should you take, the left one or the right one?"
            )
            if path_choice not in ("left", "right"):
                print("Input might be outside the provided choices. Try again")
        except ValueError:
            print("Invalid input. Try again")
        while self.player_alive and i < stages:

            decision = random.randint(1, 2)
            time.sleep(1)
            if decision == 1:
                self.player_alive = True
                print(
                    "While the room is clearly swallowed by the darkness. You were able to adapt and safely traverse the hallway without tripping on any traps. It would seem that no sentry is patrolling this area either. However, this is far from over so you continued walking forward. Not long after, much like before the path splits in front of you"
                )
            elif decision == 2:
                self.player_alive = False
                print(
                    "As soon as you entered the chamber, you felt a sharp pain in your chest be before you could make sense of what's going on, a wide gaping maw bursts out of the darkness coming straight at your direction. Alas, you were ambushed by a sentry who caught wind of your presence"
                )

            i += 1

    def decision_loop(self, stages):
        i = 0
        print(
            "After walking a barely-lit hallway without any incident, the path in front of you splits in two chambers shrouded in absolute darkness."
        )
        while self.player_alive and i < stages:
            try:
                path_choice = input(
                    "So which path should you take, the left one or the right one? "
                )
                if path_choice not in ("left", "right"):
                    print("Something went try. Try to input either left or right")
                    continue
            except ValueError:
                print("Invalid input. Try again")
                continue

            decision = random.randint(1, 2)
            time.sleep(1)

            if decision == 1:
                self.player_alive = True
                print(
                    "While the room is clearly swallowed by the darkness. You were able to adapt and safely traverse the hallway without tripping on any traps. It would seem that no sentry is patrolling this area either. However, this is far from over so you continued walking forward. Not long after, much like before the path splits in front of you"
                )
            elif decision == 2:
                time.sleep(1)
                self.player_alive = False
                defeat_cause = self.defeat_flavor()
                print(defeat_cause)

        if self.player_alive == True:
            time.sleep(1)
            print(
                "Through perseverance and perhaps some fortune, you managed to pass through several chambers safely."
            )
            time.sleep(0.5)
            print(
                "As you were about to continue forward, both your weapon and the artifact emanated a strange yet warm energy."
            )
            time.sleep(0.5)
            print(
                "It is not clear why, but you had a feeling the end is in sight so you rushed forward to the next chamber"
            )
            time.sleep(0.5)
            print(
                "Lo and behold. The once mighty and gargantuan Lubelgranz, the last king of dragons sat on a throne in the middle."
            )
            time.sleep(0.5)
            print(
                "Instead of a draconic form, he took on a more human-like wyverian form. This is a form begrudgingly used by dragons to walk amongst the other races while hiding suppressing power, be it for diplomatic or covert purposes."
            )
            time.sleep(0.5)
            print(
                "Perhaps this time around he has no choice but to settle on this due to exhausting much of his power in the last encounter against the hero."
            )
            time.sleep(0.5)
            print(
                "His appearance is that of a tired old man. Fear is clearly etched in his face. He barely has enough power to call back the sentries to his aid. Not like you would give him a chance either."
            )
            time.sleep(0.5)
            print(
                "You raised your sword and performed the move you only knew of and has practiced countless of time. Far more than the hero himself ever did. A simple downward slash, the first of the basic movements of sword fighting."
            )
            time.sleep(0.5)
            print(
                "But this is no ordinary downward slash. This is your most strongest downward slash and perhaps the strongest in the world."
            )
            time.sleep(0.5)
            print(
                "The results speak for itself, in less than a second the dragon king is cleanly bisected in half while the walls behind him are cleaved open into two allowing rays of the sun to come through."
            )
        elif self.player_alive == False:
            time.sleep(1)
            print(
                "Eventually your body is dragged to where Lubelgranz is by the sentries"
            )
            time.sleep(0.5)
            print(
                "With just one glance, Lubelgranz understood your role and that angered him for the rather shoddy attempt by the allied kingdoms to kill him"
            )
            time.sleep(0.5)
            print(
                "He swiftly separated your head from the body and ordered two of his sentries to deliver it to the allied kingdom as well as ordered to punish them for this transgression"
            )
            time.sleep(0.5)

            i += 1

    def defeat_flavor(self):
        defeat_scenes = [
            "Alas! You were caught by a sentry delivering a swift slash splitting your body into two",
            "You died! A sentry hiding in the dark out of your sight struck you in the back piercing through your heart with its spear-like tail",
            "The moment you step into the chamber the dark interior suddenly got bright as a ball of fire flies towards you. You were unable to dodge thus got incinerated to ashes",
            "Alas you were killed by a ceiling made of spikes fall on top you",
            "Alas before you could get inside the chamber, a dragon sentry pops out of the dark with it maws wide open devouring you",
        ]

        random_scene = random.choice(defeat_scenes)

        return random_scene

    def ending_scene(self):
        if self.player_alive == True:
            time.sleep(1)
            print(
                "The allied kingdoms would soon hear of news about Lubelgranz's defeat. The survivors who were once hiding in fear would step out dancing in celebration while crying tears of joy."
            )
            time.sleep(0.5)
            print(
                "Finally, for the first time in what seems forever, peace will be upon this world with the dragons now defeated"
            )
            time.sleep(0.5)
            print(
                "Alas after all that is said and done, all praises will fall on the hero who has yet to wake up after succumbing to the grave wounds inflicted by the dragons."
            )
            time.sleep(0.5)
            print(
                " For you do not exist in their consciousness. Not even a tall tale nor rumor"
            )
            time.sleep(0.5)
            print(
                "But that barely matters at all. Upon stepping out of the collapsed ruins you walked forward aimlessly away from everything else. The end."
            )
        elif self.player_alive == False:
            time.sleep(1)
            print(
                "Soon enough the world would learn of your endeavors but not in a good light."
            )
            time.sleep(0.5)
            print(
                "The survivors seeking refuge at the last bastion of the allied kingdoms would be sent in a state of chaos when two dragon sentries arrived to drop a package on a plaza."
            )
            time.sleep(0.5)
            print(
                "That package was your rotting head. The sentries would mockingly tell tales of your exploits and eventual failure."
            )
            time.sleep(0.5)
            print(
                "Then their tone shifted as they proceeded to carry out the will of their master to punish the allied races for daring to attack him. The dragons suddenly went berserk and attacked everything in sight"
            )
            time.sleep(0.5)
            print(
                "Without the hero at the front, the allied kingdoms struggled to defeat the two sentries. Eventually they did before the sun set but at the massive cost of losing a quarter of the surviving populace plus infrastructure damage"
            )
            time.sleep(0.5)
            print(
                "The remaining survivors could do nothing but fear more as the threat of the Tyrant Dragon King remains and their hero nowhere to be seen. Game over"
            )


def play_game(get_player):
    game_instance = DragonGame(get_player)
    time.sleep(1)
    keep_playing = True
    while keep_playing:
        game_instance.askplayer_mechanics()
        get_stages = game_instance.randomize_stages()
        game_instance.determine_stages(get_stages)
        game_instance.decision_loop(get_stages)
        game_instance.ending_scene()
        print(
            "Thank you for playing the game. Would you like to try again? [Y]es or [N]o"
        )
        try:
            to_continue = input(
                "Enter [Y] to continue or [N] to terminate the program "
            )
            if to_continue not in ("Y", "Yes", "yes", "N", "No", "no"):
                print("Input might be outside the provided choices. Try again")
        except ValueError:
            print("Invalid input. Try again")

        if to_continue in ("Y", "Yes", "yes", "n"):
            keep_playing = True
            game_instance.player_alive = True
        elif to_continue in ("N", "No", "no", "n"):
            keep_playing = False
            break
        else:
            print("Input Error. Terminating application")
            sys.exit(0)


if __name__ == "__main__":
    get_player = input("Tell us your name before you start this game: ")
    play_game(get_player)
