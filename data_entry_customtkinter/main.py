import customtkinter as ctk


def validate_input(text):
    if text.isdigit() and (len(text) <= 3):
        return True
    return False


def on_validate(action, value):
    if action == "1":
        return validate_input(value)
    return True


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x600")
root.title("Data Entry Form")

frame_label = ctk.CTkLabel(root, text="User Information")
frame_label.grid(row=0, column=0, padx=20, pady=(20, 0))

frame = ctk.CTkFrame(root, width=200, height=150, corner_radius=10)
frame.grid(row=1, column=0, padx=10, pady=(0, 10))

validate_command = frame.register(on_validate)

first_name_label = ctk.CTkLabel(frame, text="First Name")
first_name_label.grid(row=0, column=2, padx=10, pady=(0, 10))

last_name_label = ctk.CTkLabel(frame, text="Last Name")
last_name_label.grid(row=0, column=1, padx=10, pady=(0, 10))

middle_initial_label = ctk.CTkLabel(frame, text="Middle Initial")
middle_initial_label.grid(row=0, column=3, padx=10, pady=(0, 10))

first_name_entry = ctk.CTkEntry(frame)
first_name_entry.grid(row=1, column=2, padx=10, pady=(0, 10))

last_name_entry = ctk.CTkEntry(frame)
last_name_entry.grid(row=1, column=1, padx=10, pady=(0, 10))

middle_initial_entry = ctk.CTkEntry(frame)
middle_initial_entry.grid(row=1, column=3, padx=10, pady=(0, 10))


title_label = ctk.CTkLabel(frame, text="Title")
titles = ["", "Mr.", "Ms.", "Dr.", "Engr."]
title_combobox = ctk.CTkComboBox(frame, values=titles)

title_label.grid(row=0, column=0, padx=10, pady=(0, 10))
title_combobox.grid(row=1, column=0, padx=10, pady=(0, 10))


age_label = ctk.CTkLabel(frame, text="Age")
age_label.grid(row=0, column=4, padx=10, pady=(0, 10))
age_entry = ctk.CTkEntry(
    frame, width=50, validate="key", validatecommand=(validate_command, "%d", "%P")
)
age_entry.grid(row=1, column=4, padx=10, pady=(0, 10))

frameB_label = ctk.CTkLabel(root, text="Address Information")
frameB_label.grid(row=2, column=0, padx=20, pady=(20, 0))

frameB = ctk.CTkFrame(root, width=200, height=150, corner_radius=10)
frameB.grid(row=3, column=0, padx=10, pady=(0, 10))

addressHome_label = ctk.CTkLabel(frameB, text="Home Address")
addressHome_label.grid(row=0, column=0, padx=10, pady=(0, 10))

addressHome_entry = ctk.CTkEntry(frameB, width=700)
addressHome_entry.grid(row=1, column=0, padx=10, pady=(0, 10))

addressCurrent_label = ctk.CTkLabel(frameB, text="Current Address")
addressCurrent_label.grid(row=2, column=0, padx=10, pady=(0, 10))

addressCurrent_entry = ctk.CTkEntry(frameB, width=700)
addressCurrent_entry.grid(row=3, column=0, padx=10, pady=(0, 10))

root.mainloop()
