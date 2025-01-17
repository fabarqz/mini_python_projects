import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry as dt

window = tk.Tk()
'window.geometry("800x600")'

window.title("User Registration")

frame = tk.Frame(window)
frame.pack()

basic_info_frame = tk.LabelFrame(frame, text="Basic Information")
basic_info_frame.grid(row=0, column=0, padx=10, pady=(5, 10))

last_name_label = tk.Label(basic_info_frame, text="Last Name")
last_name_label.grid(row=0, column=0)

first_name_label = tk.Label(basic_info_frame, text="First Name")
first_name_label.grid(row=0, column=1)

middle_name_label = tk.Label(basic_info_frame, text="Middle Name")
middle_name_label.grid(row=0, column=2)

suffix_label = tk.Label(basic_info_frame, text="Suffix")
suffix_label.grid(row=0, column=3)

age_label = tk.Label(basic_info_frame, text="Age")
age_label.grid(row=0, column=4)

last_name_entry = tk.Entry(basic_info_frame)
last_name_entry.grid(row=1, column=0)

first_name_entry = tk.Entry(basic_info_frame)
first_name_entry.grid(row=1, column=1)

middle_name_entry = tk.Entry(basic_info_frame)
middle_name_entry.grid(row=1, column=2)

suffixes = ["", "Sr.", "Jr", "I", "II", "III", "IV"]

suffix_entry = ttk.Combobox(basic_info_frame, width=4, values=suffixes)
suffix_entry.grid(row=1, column=3)


age_spinbox = ttk.Spinbox(basic_info_frame, from_=1, to=100, width=5)
age_spinbox.grid(row=1, column=4)


dob_label = tk.Label(basic_info_frame, text="Date of Birth")
dob_label.grid(row=2, column=0)

dob_entry = dt(basic_info_frame, width=16)
dob_entry.grid(row=30, column=0)

window.mainloop()
