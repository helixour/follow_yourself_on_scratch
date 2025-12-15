import scratchattach as sa
from customtkinter import *
import warnings

print("Loading...")

root = CTk()
root.title("Follow yourself on Scratch")
root.resizable(False, False)
root.geometry("235x175")
set_appearance_mode("System")


warnings.filterwarnings('ignore', category=sa.LoginDataWarning)


def get_entry_value():
    user = user_box.get()
    password = pass_box.get()
    try:
        session = sa.login(user, password)
        user = session.connect_user(user)
        user.follow()
        print("Done! Check your followers on Scratch. You can close this now")
    except sa.utils.exceptions.LoginFailure:
        print("Account does not exist or you made a typo in your username or password")


user_box = CTkEntry(
    master=root,
    placeholder_text="Scratch Username",
    corner_radius=10,
    width=200,
    height=40,
    border_width=2,
    fg_color=("white", "gray75")
)
user_box.pack(pady=10)


pass_box = CTkEntry(
    master=root,
    placeholder_text="Scratch Password",
    corner_radius=10,
    width=200,
    height=40,
    border_width=2,
    fg_color=("white", "gray75")
)
pass_box.pack(pady=10)


submit_button = CTkButton(master=root,
    corner_radius=10,
    command=get_entry_value,
    text="Sign In",
    width=120,
    height=40,
    border_width=0,
    fg_color="#0078ff",
    hover_color="#0056b3")
submit_button.pack(pady=10)

root.mainloop()