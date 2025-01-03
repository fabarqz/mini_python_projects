import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("800x600")
root.title("Data Entry Form")

frame = customtkinter.CTkFrame(root)


user_info_frame = customtkinter.CTkLabel(master=frame, text="User Information")
user_info_frame.grid(row=0, column=0)

first_name_label = customtkinter.CTkLabel(master=frame, text="First Name")
user_info_frame.grid(row=0, column=0)
frame.pack()
root.mainloop()
