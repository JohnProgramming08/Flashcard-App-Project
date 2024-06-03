import customtkinter as ctk
from display import LoginPage, HomePage
from login_function import sign_up
from database_management import get_stats

def main():
  #setting up root window
  ctk.set_appearance_mode("dark")
  ctk.set_default_color_theme("blue")
  root = ctk.CTk()
  root.title("Revision App")
        
  login_page1 = LoginPage(root, "")
  login_page1.create_frames()
  login_page1.create_widgets()

  #displays an error message
  def error_message(message):
    error_window = ctk.CTkToplevel(root, fg_color="red")
    error_window.title("Error")
    error = ctk.CTkLabel(error_window, text=message)
    error.pack()

  #if the username is valid, creates new account 
  def sign_up2():
    username = login_page1.username_entry.get()
    password = login_page1.password_entry.get()
    attempt = sign_up(username, password)
    if attempt == True:
      stats = get_stats(username)
      home_page = HomePage(root, stats[1], stats[2], stats[3])
      home_page.create_frames()
      home_page.create_widgets()
      login_page1.change_pages(login_page1.login_page, home_page.page_tabs)

    #returns an appropriate error message 
    elif attempt == "used":
      error_message("Username already taken")

    else:
      error_message("Spaces are not allowed")
      
  login_page1.sign_up_button.configure(command=sign_up2)
  root.mainloop()

if __name__ == "__main__":
  main()