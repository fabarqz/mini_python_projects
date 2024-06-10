import os
import sys
from time import sleep
from pynput import keyboard
import keyboard as keyb


def delete_last_line():
    sys.stdout.write("\x1b[1A")
    sys.stdout.write("\x1b[2k")


def fancy_print(x: str) -> str:
    pass


def typingEffect(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.05)


def wait_for_enter():
    def on_press(key):
        if key == keyboard.Key.enter:
            return False  # Stop the listener

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def ask_yes_no():
    if keyb.read_key() == "y":
        typingEffect("You have chosen yes")
    elif keyb.read_key() == "n":
        typingEffect("Alas. You picked no")


if __name__ == "__main__":
    typingEffect("This is a test text. Follow the instruction on the next line\n")
    typingEffect("Press enter to continue\n")
    wait_for_enter()
    delete_last_line()
    typingEffect("The last line should have been deleted\n")
    typingEffect("Question, Yes or No?\n")
    ask_yes_no()
