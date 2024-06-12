from os import system
from sys import stdout
from time import sleep
from pynput import keyboard as board
import keyboard
import pyfiglet


class Fancy:
    def __init__(self):
        self.number_of_lines = 0

    def get_name(self):
        self.printLine("Please enter your name: ")
        self.name = input()
        fancy.delete_one_line()
        fancy.printLine(f"\rWelcome, {fancy.name}")

    def delete_one_line(self):
        stdout.write("\x1b[1A")
        stdout.write("\x1b[2k")
        self.typingEffect(" " * 50)
        stdout.write("\x1b[1A")
        print("\r")

    def replace_previous_line(self, text):
        stdout.write("\x1b[1A")
        stdout.write("\r\n")
        self.printLine(text)

    def replace_line(self, text):
        stdout.write("\x1b[1A")
        self.typingEffect(text)

    def typingEffect(self, text):
        for character in text:
            stdout.write(character)
            stdout.flush()
            sleep(0.05)

    def printLine(self, text):
        self.number_of_lines += 1
        return self.typingEffect(text)

    def print_banner(self):
        self.banner = pyfiglet.figlet_format("This is a banner", font="digital")
        self.banner_count = self.banner.count("\n") + 1
        print(self.banner)

    def clear_terminal(self):
        print("\033c", end="")
        fancy.print_banner()


if __name__ == "__main__":
    # clears the terminal first. this primarily is for executing the code in command prompt. as observed, the vscode terminal has no issues with this to some extent
    system("cls")
    fancy = Fancy()
    fancy.print_banner()
    fancy.printLine("This is a line\n")
    fancy.printLine("The terminal will be reset")
    sleep(5)
    fancy.clear_terminal()
    fancy.printLine("This is a new line after the reset")

    # fancy.get_name()
    # fancy.replace_previous_line("This text should replace the previous line")
    # fancy.printLine(f"Just checking. You are {fancy.name}, right?")
