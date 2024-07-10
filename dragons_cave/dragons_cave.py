from os import system
from sys import stdout, stdin
from time import sleep
from pynput import keyboard as board
import keyboard
import pyfiglet
import random


class Game:
    def __init__(self, player_name):
        self.player_name = player_name

        self.player_alive = True
        self.player_alive = True

        self.debug_enabled = False
        self.stages = self.generate_stages()
        self.dungeon_solution = self.generate_dungeon()

        self.game_text = {
            "main_menu": {
                "line_a": f"Greetings {self.player_name}, Choose the number of the action you wish to do below.\n",
                "line_b": "[1] Learn more about the lore.\n",
                "line_c": "[2] Learn more about the game mechanics.\n",
                "line_d": "[3] Start game.\n",
            },
            "lore_menu": {
                "line_a": "Choose below which lore topic do you wish to learn more of:\n",
                "line_b": "[1] On Volgrand\n",
                "line_c": "[2] On Abelion\n",
                "line_d": "[3] On The Hidden Blade Order\n",
            },
            "lore_menu_dragon": {
                "line_a": "Three thousand years ago, a dragon whelp named Vol would came into being.\n",
                "line_b": "As a youngling, Vol stood out amongst his fellow kin for his shiny obsidian-like scales that glimmer like the night sky.\n",
                "line_c": "But unbeknownst to all, this young dragon turns out to be the most ambitious and vile existence to walk the land\n",
                "line_d": "Through walking a path of bloodshed and violence, the dragon race was reduced from a majestic beings respected by all to an army that carry out his tyrannical will",
                "line_e": "His prismatic black scales would soon be tainted with red streaks glowing ominously. He then would change his name from Vol to Volgrand and naming himself as the Dragon King.",
                "line_f": "As dragon king, his first edict is to wage war against the rest of the world. Through his will, dragons soared through the skies wreaking havoc and enslaving the other races they defeated",
            },
            "lore_menu_alliance": {
                "line_a": "Though Volgrand's bloody campaign for conquest nearly wiped out everyone off the face of the planet, the rest of the races the tyrannical dragon king viewed as inferior didn't back down resisted his forces\n",
                "line_b": "The once separated races eventually managed to unite forming an alliance despite its very shaky foundation.\n",
                "line_c": "It was spearheaded by the Humans, Elves, and Dwarves by virtue of being the most populous races",
                "line_d": "They would later be joined by the other smallfolk such as gnomes, hobbits, and halflings\n",
                "line_e": "Almost half of the beastmen races who escaped the enslavement of Volgrand's Army.\n",
                "line_c": "The various merfolk and the descendants of the spirits, Fae would join this alliance last.\n",
            },
            "lore_menu_hero": {},
            "mechanics_menu": {
                "line_a": "The path between you and the enemy is divided into a random number of stages.\n",
                "line_b": "Each stage splits to up to three paths and you must pick the right path to pass through safely.\n",
                "line_c": "Despite being next to the hero in terms of strength, you are still fragile against the patrolling sentries protecting the dragon king as well as the traps they set up all over the dungeon\n",
                "line_d": "Thus avoiding confrontation with the sentries as well as avoiding triggering any trap is a must\n",
                "line_e": "To achieve victory, you must pass through all stages undetected and safe until you reach the dragon king's chamber\n",
                "line_f": "Only then can you unleash your full strength to finish what the hero has started by putting an end to the dragon king's life and their race's reign of terror\n",
            },
            "ask": {"return_menu": "Do you wish to return to the main menu?"},
            "game_start": {
                "line_a": "The end of the Volgrand's tyrannical rule is nigh.\n",
                "line_b": "But alas, it would seem the evil dragon still has its clutches over its fate and refusing to go down to the very end.\n",
                "line_c": "Despite giving his all, the Hero Orland failed to kill the dragon king.\n",
                "line_d": "To add salt to the injury, the dragon used the confusion caused by the hero collapsing after unleashing the attack that was supposed to kill him to make a cowardly escape instead.\n",
                "line_e": "Almost all of Volgrand's forces have been defeated, leaving the tyrannical dragon the only thing left threatening this world.\n",
                "line_f": "But he is Volgrand, the strongest being that sent the world into chaos for three thousand years.\n",
                "line_g": "He can and will regain the powers he lost in its war against the Hero and the Alliance. As to when, only he can know\n",
                "line_h": "As such this was less of a victory on the Alliance side and more of a stalemate. Both the hero and the evil dragon are out of commission\n",
                "line_i": f"This is where your part comes, Ser {self.player_name}. As the sole survivor of the Hidden Blade Order, you are commissioned to seek out where Volgrand is hiding\n",
                "line_j": "This is a perilous task only known to the higher ups in the Alliance. \n",
                "line_k": "You find yourself before the entrance of a great ancient ruins far south of the Royal Kingdom of Algon.\n",
                "line_l": "It has yet to be named but according to the mages you met before setting of for this mission it must predate even the conquest of Volgrand.\n",
                "line_m": "History aside. There's nothing stationed at the door but the ominous aura emitted by the draconic beings though faint can be felt deep within the ruins.\n",
                "line_n": "Wasting no time, you proceed to enter the ruins with great determination to end this.\n",
                "line_o": "The ruins is shrouded in darkness but you as a Hidden Blade you should be able to manage to traverse the however many chambers separating you and the dragon.\n",
            },
            "defeat": {
                "line_a": "Alas! You were caught by a sentry delivering a swift slash splitting your body into two\n",
                "line_b": "You died! A sentry hiding in the dark out of your sight struck you in the back piercing through your heart with its spear-like tail\n",
                "line_c": "The moment you step into the chamber the dark interior suddenly got bright as a ball of fire flies towards you. You were unable to dodge thus got incinerated to ashes\n",
                "line_d": "Alas you were killed by a ceiling made of spikes fall on top you\n",
                "line_e": "Alas before you could get inside the chamber, a dragon sentry pops out of the dark with it maws wide open devouring you\n",
            },
            "pass_safely": {
                "line_a": "While the foreboding air is there, this room is oddly devoid of traps nor is there a sentry patrolling. Nevertheless, you maintain your guard and carefully walk towards the exit.\n",
                "line_b": "You traversed through the dark chamber safely. It is however not without hardship as you have to carefully walk so as to not trip any of the pressure plates scattered about the room.\n ",
                "line_c": "There doesn't seem to be any form of traps in this room. However you hear faint draconic growls echoing through the hall. It must be coming from the other chambers. You proceed to traverse the room with haste ensuring to not make a noise that would alert the sentry of your presence.\n",
            },
        }

    def clear_keyboard(self):
        stdin.flush()
        sleep(0.01)

    def print_banner(self):
        self.banner = pyfiglet.figlet_format("Dragon's Dead End ", font="digital")
        self.banner_count = self.banner.count("\n") + 1
        print(self.banner)
        if self.debug_enabled == True:
            print(self.dungeon_solution)

    def clear_terminal(self):
        print("\033c", end="")
        self.print_banner()

    def print_line(self, text):
        for character in text:
            stdout.write(character)
            stdout.flush()
            sleep(0.035)

    def ask_yes_no(self):
        if keyboard.read_key() == "y":
            self.print_line("You have chosen yes")
            keyboard.clearEvents()
        elif keyboard.read_key() == "n":
            self.print_line("Alas. You picked no")

    # Game sections
    def game_intro(self):
        self.print_banner()
        self.print_line("A text-based adventure game written in Python")
        sleep(0.5)
        self.clear_terminal()

    def ask_mechanics(self):
        self.print_line(f"Do you wish to hear the mechanics, Sir {self.player_name}?\n")
        if keyboard.read_key() == "y":
            self.clear_keyboard()
            self.roll_mechanics()

        elif keyboard.read_key() == "n":
            self.clear_keyboard()
            self.print_line("Alas. You picked no")

    def choice_lore(self):
        self.clear_keyboard()
        self.roll_lore()
        sleep(0.25)
        self.ask_return_menu()

    def ask_return_menu_alt(self):
        self.clear_terminal()
        self.print_line(self.game_text["ask"].get("return_menu"))
        if keyboard.read_key() == "y":
            self.clear_keyboard()
            self.main_menu()
        elif keyboard.read_key() == "n":
            self.clear_keyboard()
            self.print_line("Alas. You picked no")

    def ask_return_menu(self):
        self.player_alive = True
        self.stages = self.generate_stages()
        self.dungeon_solution = self.generate_dungeon()

        self.clear_terminal()
        self.print_line(self.game_text["ask"].get("return_menu"))
        while True:
            return_choice = input("\nYour choice is (y or n) ").strip().lower()
            if return_choice == "y":
                self.clear_keyboard()
                self.main_menu()
            elif return_choice == "n":
                self.clear_keyboard()
                self.print_line("Alas. You picked no. Closing app")
                sleep(0.5)
                break

    def print_game_text(self, key):
        for sub_key, value in self.game_text[key].items():
            self.print_line(value)
            sleep(0.075)

    def main_menu_alt(self):
        self.clear_keyboard()
        self.clear_terminal()
        self.print_game_text("main_menu")
        correct_input = False
        while not correct_input:
            try:
                if keyboard.read_key() == "1":
                    sleep(0.25)
                    self.choice_lore()

                elif keyboard.read_key() == "2":
                    sleep(0.25)
                    self.clear_keyboard()
                    self.roll_mechanics()
                    correct_input = True
                elif keyboard.read_key() == "3":
                    sleep(0.25)
                    self.clear_keyboard()
                    self.clear_terminal()
                    self.print_line("To follow")
                    correct_input = True
                else:
                    raise ValueError("Error! Your choice is not in the option\n")
            except ValueError as error:
                self.print_line(str(error))

    def main_menu(self):
        self.clear_keyboard()
        self.clear_terminal()
        self.print_game_text("main_menu")
        while True:
            user_menu_choice = input("The choice is ")
            try:
                if user_menu_choice in {"1", "2", "3", "debug"}:
                    break
                else:
                    raise ValueError("Input Error. Try again.")
            except ValueError as error:
                self.print_line(str(error))
        self.run_menu_choice(user_menu_choice)

    def lore_menu(self):
        self.clear_keyboard()
        self.clear_terminal()
        self.print_game_text("lore_menu")
        while True:
            user_menu_choice = int(input("The choice is "))
            try:
                if user_menu_choice in {1, 2, 3}:
                    break
                else:
                    raise ValueError("Input Error. Try again.")
            except ValueError as error:
                self.print_line(str(error))
        self.run_lore_choice(user_menu_choice)

    def run_menu_choice(self, choice):
        if choice == "1":
            sleep(0.25)
            self.clear_terminal()
            self.lore_menu()

        elif choice == "2":
            sleep(0.25)
            self.clear_terminal()
            self.roll_mechanics()

        elif choice == "3":
            sleep(0.25)
            self.clear_terminal()
            self.roll_start_text()
            # self.game_loop()

        elif choice == "debug":
            sleep(0.25)
            self.print_line("debug mode enabled")
            self.debug_enabled = True
            self.ask_return_menu()

    def run_lore_choice(self, choice):
        if choice == 1:
            sleep(0.25)
            self.clear_terminal()
            self.choice_lore()

        elif choice == 2:
            sleep(0.25)
            self.clear_terminal()
            self.roll_mechanics()

        elif choice == 3:
            sleep(0.25)
            self.clear_terminal()
            self.print_line("To follow")

    def roll_mechanics(self):
        self.clear_terminal()
        self.print_game_text("mechanics_menu")

    def roll_lore(self):
        self.clear_terminal()
        self.print_game_text("lore_menu_dragon")

    def roll_start_text(self):
        self.clear_terminal()
        self.print_game_text("game_start")
        self.game_loop()

    def play_game(self):
        self.game_intro()
        sleep(0.05)
        # self.ask_mechanics()
        self.main_menu()

    def game_loop(self):
        self.clear_terminal()
        sleep(0.05)
        self.dungeon_loop()

    def generate_stages(self):
        return random.randint(4, 12)

    def generate_dungeon(self):
        chambers = ["left", "middle", "right"]
        self.dungeon_solution = [random.choice(chambers) for x in range(self.stages)]
        return self.dungeon_solution

    def get_choice(self, solution):
        try:
            if solution in ("left", "right"):
                self.print_line(
                    "The path before you splits into two, will you take the left or right path? "
                )
                chamber = input().strip().lower()
                if chamber not in ["left", "right", "Left", "Right"]:
                    raise ValueError(
                        "Invalid input. You can only pick between left and right"
                    )
            elif solution == "middle":
                self.print_line(
                    "The path before you splits into three, will you take the left,middle or right path? "
                )
                chamber = input().strip().lower()
                if chamber not in [
                    "left",
                    "right",
                    "Left",
                    "Right",
                    "middle",
                    "Middle",
                ]:
                    raise ValueError(
                        "Invalid input. You can only pick either left ,middle or right"
                    )
            return chamber
        except ValueError as e:
            print(e)

    def get_random_defeat(self):
        defeat_messages = self.game_text["defeat"]
        random_key = random.choice(list(defeat_messages.keys()))
        return defeat_messages[random_key]

    def get_random_pass(self):
        pass_messages = self.game_text["pass_safely"]
        random_key = random.choice(list(pass_messages.keys()))
        return pass_messages[random_key]

    def dungeon_loop(self):
        current_dungeon = self.dungeon_solution
        for level in current_dungeon:
            if not self.player_alive:
                self.print_line("Alas! You have died.")
                self.ask_return_menu()
            chosen_chamber = self.get_choice(level)
            if chosen_chamber == level:
                self.print_line(self.get_random_pass())
            else:
                self.print_line(self.get_random_defeat())
                self.player_alive = False


if __name__ == "__main__":

    get_player = input("Before we start kindly tell us your name: ")
    game = Game(get_player)
    sleep(0.75)
    print("\033c", end="")
    game.play_game()
