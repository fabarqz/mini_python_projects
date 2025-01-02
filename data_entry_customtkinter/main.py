import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("800x600")
root.title("Data Entry Form")

frame = customtkinter.CTkFrame(root)
frame.pack()

user_info_frame = customtkinter.CTkLabel(master=frame, text="User Inframe")
user_info_frame.grid(row=0, colunmn=0)

first_name_label = customtkinter.CTkFrame(user_info_frame, text="First Name")


root.mainloop()
