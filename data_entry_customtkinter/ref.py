import tkinter as tk

window = tk.Tk()
window.geometry("800x600")

window.title("User Registration")

frame = tk.Frame(window)
frame.pack()

basic_info_frame = tk.LabelFrame(frame, text="Basic Information")

window.mainloop()
