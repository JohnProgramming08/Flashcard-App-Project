import customtkinter as ctk
from display import IntroPage, HomePage, App
from intro_function import sign_up, login
from database_management import get_stats

def main():
  app = App()
  #if the username is valid, creates new account 
  def sign_up2():
    username = app.intro_page.username_entry.get()
    password = app.intro_page.password_entry.get()
    attempt = sign_up(username, password)
    if attempt is True:
      stats = get_stats(username)
      app.home_page = HomePage(app.home_tab, stats[2], stats[1], stats[3])
      app.intro_page.change_pages(app.intro_page, app.tabs)

    #returns an appropriate error message 
    elif attempt == "used":
      app.error_message("Username already taken")

    else:
      app.error_message("Spaces are not allowed")
      
  app.intro_page.sign_up_button.configure(command=sign_up2)

  
  def login2():
    #if details are valid, logs in
    username = app.intro_page.username_entry.get()
    password = app.intro_page.password_entry.get()
    if login(username, password) is True:
      stats = get_stats(username)
      app.home_page = HomePage(app.home_tab, stats[2], stats[1], stats[3])
      app.intro_page.change_pages(app.intro_page, app.tabs)

    #returns an appropriate error message
    else:
      app.error_message("Incorrect username or password")

  app.intro_page.login_button.configure(command=login2)
  app.mainloop()

if __name__ == "__main__":
  main()