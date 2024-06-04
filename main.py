import customtkinter as ctk
from display import LoginPage, HomePage, App
from login_function import sign_up
from database_management import get_stats

def main():
  app = App()
  #if the username is valid, creates new account 
  def sign_up2():
    username = app.login_page.username_entry.get()
    password = app.login_page.password_entry.get()
    attempt = sign_up(username, password)
    if attempt is True:
      stats = get_stats(username)
      app.home_page = HomePage(app.home_tab, stats[2], stats[1], stats[3])
      app.login_page.change_pages(app.login_page, app.tabs)

    #returns an appropriate error message 
    elif attempt == "used":
      app.error_message("Username already taken")

    else:
      app.error_message("Spaces are not allowed")
      
  app.login_page.sign_up_button.configure(command=sign_up2)
  app.mainloop()

if __name__ == "__main__":
  main()