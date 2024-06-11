from sys import stdout
from time import sleep
from pynput import keyboard as board
import keyboard


class Fancy:
    def __init__(self):
        self.number_of_lines = 0

    def delete_one_line(self):
        stdout.write("\x1b[1A")
        stdout.write("\x1b[2k")
        self.typingEffect(" " * 50)

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


if __name__ == "__main__":
    fancy = Fancy()
    fancy.printLine("This is a testLine\n")
    sleep(1)
    fancy.printLine("This is a another line\n")
    sleep(1)
    fancy.printLine("This third line will soon be deleted\n")
    sleep(1)
    # fancy.delete_one_line()
    # fancy.printLine("\nThis a new line")
    fancy.replace_line("This line replaces the previously deleted line")
