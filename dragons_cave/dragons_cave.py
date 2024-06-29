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
            "lore_menu_hero": {
                "line_a": "Though Volgrand's bloody campaign for conquest nearly wiped out everyone off the face of the planet, the rest of the races the tyrannical dragon king viewed as inferior didn't back down without a fight\n",
            },
            "mechanics_menu": {
                "line_a": "The path between you and the enemy is divided into a random number of stages.\n",
                "line_b": "Each stage splits to up to three paths and you must pick the right path to pass through safely.\n",
                "line_c": "Despite being next to the hero in terms of strength, you are still fragile against the patrolling sentries protecting the dragon king as well as the traps they set up all over the dungeon\n",
                "line_d": "Thus avoiding confrontation with the sentries as well as avoiding triggering any trap is a must\n",
                "line_e": "To achieve victory, you must pass through all stages undetected and safe until you reach the dragon king's chamber\n",
                "line_f": "Only then can you unleash your full strength to finish what the hero has started by putting an end to the dragon king's life and their race's reign of terror\n",
            },
            "ask": {"return_menu": "Do you wish to return to the main menu?"},
            "defeat": {
                "line_a": "Alas! You were caught by a sentry delivering a swift slash splitting your body into two\n",
                "line_b": "You died! A sentry hiding in the dark out of your sight struck you in the back piercing through your heart with its spear-like tail\n",
                "line_c": "The moment you step into the chamber the dark interior suddenly got bright as a ball of fire flies towards you. You were unable to dodge thus got incinerated to ashes\n",
                "line_d": "Alas you were killed by a ceiling made of spikes fall on top you\n",
                "line_e": "Alas before you could get inside the chamber, a dragon sentry pops out of the dark with it maws wide open devouring you\n",
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
        self.clear_terminal()
        self.print_line(self.game_text["ask"].get("return_menu"))
        while True:
            return_choice = input("\nYour choice is (y or n) ").strip().lower()
            if return_choice == "y":
                self.clear_keyboard()
                self.main_menu()
            elif return_choice == "n":
                self.clear_keyboard()
                self.print_line("Alas. You picked no")

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
            self.game_loop()

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
                chamber = (
                    input(
                        "The path before you splits into two, will you take the left or right path?"
                    )
                    .strip()
                    .lower()
                )
                if chamber not in ["left", "right", "Left", "Right"]:
                    raise ValueError(
                        "Invalid input. You can only pick between left and right"
                    )
            elif solution == "middle":
                chamber = (
                    input(
                        "The path before you splits into three, will you take the left,middle or right path?"
                    )
                    .strip()
                    .lower()
                )
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

    def dungeon_loop(self):
        current_dungeon = self.dungeon_solution
        for level in current_dungeon:
            if not self.player_alive:
                break
            chosen_chamber = self.get_choice(level)
            if chosen_chamber == level:
                self.print_line(
                    "You picked the correct path so you can proceed further"
                )
            else:
                self.print_line("You died")
                self.player_alive = False
                break


if __name__ == "__main__":

    get_player = input("Before we start kindly tell us your name: ")
    game = Game(get_player)
    sleep(0.75)
    print("\033c", end="")
    game.play_game()
