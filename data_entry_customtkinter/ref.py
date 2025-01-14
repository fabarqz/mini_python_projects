import tkinter as tk

window = tk.Tk()
window.geometry("800x600")

window.title("User Registration")

frame = tk.Frame(window)
frame.pack()

basic_info_frame = tk.LabelFrame(frame, text="Basic Information")
basic_info_frame.grid(row=0, column=0)

last_name_label = tk.Label(basic_info_frame, text="Last Name")
last_name_label.grid(row=0, column=0)

first_name_label = tk.Label(basic_info_frame, text="First Name")
first_name_label.grid(row=0, column=1)

middle_name_label = tk.Label(basic_info_frame, text="Middle Name")
middle_name_label.grid(row=0, column=2)

suffix_label = tk.Label(basic_info_frame, text="Suffix")
suffix_label.grid(row=0, column=3)

last_name_entry = tk.Entry(basic_info_frame)
last_name_entry.grid(row=1, column=0)

first_name_entry = tk.Entry(basic_info_frame)
first_name_entry.grid(row=1, column=1)

middle_name_entry = tk.Entry(basic_info_frame)
middle_name_entry.grid(row=1, column=2)

suffix_entry = tk.Entry(basic_info_frame, width=4)
suffix_entry.grid(row=1, column=3)

window.mainloop()
