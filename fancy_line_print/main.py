import os
import sys
from time import sleep
from pynput import keyboard


def delete_last_line():
    sys.stdout.write("\x1b[1A")
    sys.stdout.write("\x1b[2k")


def fancy_print(x: str) -> str:
    pass


def is_enter(key):
    if key == keyboard.Key.enter:
        return False


if __name__ == "__main__":
    print("This is a test text. Follow the instruction on the next line")
    delete_last_line()
    print("The last line should have been deleted")
