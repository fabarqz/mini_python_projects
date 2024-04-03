import tkinter as tk
import pyperclip
import random
import string


def generate_password(length_entry, password_entry):
    password_length = length_entry.get()
    if password_length.isdigit() and int(password_length) > 0:
        password = "".join(
            random.choices(
                string.ascii_letters + string.digits + string.punctuation,
                k=int(password_length),
            )
        )
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Invalid password length")


def copy_password(password_entry):
    password = password_entry.get()
    pyperclip.copy(password)


def main():
    window = tk.Tk()
    window.title("Password Generator")
    window.minsize(300, 220)

    length_label = tk.Label(window, text="Password Length")
    length_label.pack(pady=10)
    length_entry = tk.Entry(window, width=6)
    length_entry.pack(pady=5)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    generate_button = tk.Button(
        button_frame,
        text="Generate Password",
        command=lambda: generate_password(length_entry, password_entry),
    )
    generate_button.pack(side=tk.LEFT, pady=10)
    # generate_button.grid(column=0, row=0)
    copy_button = tk.Button(
        button_frame,
        text="Copy Passowrd",
        command=lambda: copy_password(password_entry),
    )
    copy_button.pack(side=tk.RIGHT)

    password_label = tk.Label(window, text="Generated Password:")
    password_label.pack()
    password_entry = tk.Entry(window, width=30)
    password_entry.pack(pady=5)

    window.mainloop()


main()
