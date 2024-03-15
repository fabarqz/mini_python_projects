import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window, text_edit):
    filepath = askopenfilename(
        filetypes=[
            ("Text Files", "*.txt"),
            ("Markdown Files", "*.md"),
            ("HTML Files", "*.html"),
            ("All Files", "*"),
        ]
    )

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)

    window.title(f"Open File {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Markdown Files", "*.md"),
            ("HTML Files", "*.html"),
            ("All Files", "*"),
        ],
    )

    if not filepath:
        return

    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)

    window.title(f"Save as: {filepath}")


def main():
    window = tk.Tk()
    window.title("Simple Text Editor")
    window.rowconfigure(0, minsize=300)
    window.columnconfigure(1, minsize=150)

    font_tuple = ("Comic Sans MS", 10, "bold")
    text_edit = tk.Text(window, font=font_tuple)
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=1)
    save_button = tk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit)
    )
    open_button = tk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit)
    )

    save_button.grid(row=0, column=0, padx=3, pady=3, sticky="ew")
    open_button.grid(row=1, column=0, padx=3, pady=3, sticky="ew")

    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()


main()
