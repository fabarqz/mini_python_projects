from os import system
from sys import stdout
from time import sleep
from pynput import keyboard as board
import keyboard
import pyfiglet


class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_alive = True
        self.game_text = {
            "main_menu": {
                "line_a": f"Greetings {self.player_name}, Choose the number of the action you wish to do below.\n",
                "line_b": "[1] Learn more about the lore.\n",
                "line_c": "[2] Learn more about the game mechanics.\n",
                "line_d": "[1] Start game.\n",
            },
            "mechanics_menu": {
                "line_a": "The path between you and the enemy is divided into a random number of stages.\n",
                "line_b": "Each stage splits to up to three paths and you must pick the right path to pass through safely.\n",
                "line_c": "Despite being next to the hero in terms of strength, you are still fragile against the patrolling sentries protecting the dragon king as well as the traps they set up all over the dungeon\n",
                "line_d": "Thus avoiding confrontation with the sentries as well as avoiding triggering any trap is a must\n",
                "line_e": "To achieve victory, you must pass through all stages undetected and safe until you reach the dragon king's chamber\n",
                "line_f": "Only then can you unleash your full strength to finish what the hero has started by putting an end to the dragon king's life and their race's reign of terror\n",
            },
        }

    def print_banner(self):
        self.banner = pyfiglet.figlet_format("Dragon's Dead End ", font="digital")
        self.banner_count = self.banner.count("\n") + 1
        print(self.banner)

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
            self.roll_mechanics()
        elif keyboard.read_key() == "n":
            self.print_line("Alas. You picked no")

    def print_game_text(self, key):
        for sub_key, value in self.game_text[key].items():
            self.print_line(value)
            sleep(0.075)

    def main_menu(self):
        self.print_game_text("main_menu")
        try:
            if keyboard.read_key() == "1":
                sleep(0.25)
                self.clear_terminal()
                self.print_line("To follow")
            elif keyboard.read_key() == "2":
                sleep(0.25)
                self.roll_mechanics()
            elif keyboard.read_key == "3":
                sleep(0.25)
                self.clear_terminal()
                self.print_line("To follow")
            else:
                raise ValueError("Error! Your choice is not in the option")
        except ValueError as error:
            self.print_line(str(error))

    def roll_mechanics(self):
        self.print_game_text("mechanics_menu")

    def play_game(self):
        self.game_intro()
        sleep(0.05)
        # self.ask_mechanics()
        self.main_menu()


if __name__ == "__main__":

    get_player = input("Before we start kindly tell us your name: ")
    game = Game(get_player)
    sleep(0.75)
    print("\033c", end="")
    game.play_game()
