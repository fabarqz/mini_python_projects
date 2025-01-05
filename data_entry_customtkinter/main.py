import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x600")
root.title("Data Entry Form")

frame_label = ctk.CTkLabel(root, text="User Information")
frame_label.grid(row=0, column=0, padx=20, pady=(20, 0))

frame = ctk.CTkFrame(root, width=200, height=150, corner_radius=10)
frame.grid(row=1, column=0, padx=10, pady=(0, 10))

first_name_label = ctk.CTkLabel(frame, text="First Name")
first_name_label.grid(row=0, column=0, padx=10, pady=(0, 10))

last_name_label = ctk.CTkLabel(frame, text="Last Name")
last_name_label.grid(row=0, column=1, padx=10, pady=(0, 10))

first_name_entry = ctk.CTkEntry(frame)
first_name_entry.grid(row=1, column=0, padx=10, pady=(0, 10))
root.mainloop()
