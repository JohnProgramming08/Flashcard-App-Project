import customtkinter as ctk
from display import LoginPage, HomePage
from login_function import sign_up

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Revision App")

login_page = LoginPage(root, sign_up)
login_page.create_frames()
login_page.create_widgets()

def sign_up2():
    username = login_page.username_entry.get()
    password = login_page.password_entry.get()
    if sign_up(username, password):
            home_page = HomePage(root, 0, 0, 0)
            home_page.create_frames()
            home_page.create_widgets()
            login_page.change_pages(login_page.login_page, home_page.page_tabs)
    else:
      return False

login_page.login_button.configure(command=sign_up2)

root.mainloop()