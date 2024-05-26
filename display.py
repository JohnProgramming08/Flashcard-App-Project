import customtkinter as ctk


class Page:
  def __init__(self, window):
    self.root = window
    self.page = ctk.CTkFrame(self.root)
    self.title_font = ctk.CTkFont(family="Roboto", size=20, weight="bold", underline=True)
    self.heading_font = ctk.CTkFont(family="arial", size=14, weight="bold")
    self.normal_font = ctk.CTkFont(family="arial", size=13)

  #creates all frames meeded for page
  def create_frames(self):
    pass

  #creates widgets needed for page
  def create_widgets(self):
    pass

  #changes pages
  def change_pages(self, current_page, next_page):
    current_page.remove()
    next_page.pack()


class LoginPage(Page):
  def __init__(self, window):
      super().__init__(window)
      self.login_page = ctk.CTkFrame(self.root)
      self.login_page.pack()

  #creates frames for the login page
  def create_frames(self):
    self.information_frame = ctk.CTkFrame(self.login_page)
    self.information_frame.grid(row=0, column=0, padx=20, pady=20)
    self.login_frame = ctk.CTkFrame(self.login_page)
    self.login_frame.grid(row=0, column=1, padx=20, pady=20)
    self.contact_frame = ctk.CTkFrame(self.login_page)
    self.contact_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

  #creates widgets for the login page
  def create_widgets(self):
    self.title = ctk.CTkLabel(self.information_frame, text="Information", font=self.title_font)
    self.title.grid(row=0, column=0)

    #55 characters per line
    self.purpose = ctk.CTkLabel(self.information_frame, text="This is a revision/study app to help UK students revise.\n", font=self.heading_font)
    self.purpose.grid(row=1, column=0, padx=5)
    self.purpose2 = ctk.CTkLabel(self.information_frame, text="This app has spaced repetition algorithms, downloadable\npast papers, quizes and more! If you would wish to try\nit out then please press sign in.", font=self.normal_font)
    self.purpose2.grid(row=2, column=0, padx=5)

    #contact information
    self.contact_title = ctk.CTkLabel(self.contact_frame, text="Contact", font=self.title_font)
    self.contact_title.grid(row=0, column=0)

    self.contact_purpose = ctk.CTkLabel(self.contact_frame, text="If you have any questions or concerns please contact me at: dylan08code.gmail.com", font=self.heading_font)
    self.contact_purpose.grid(row=1, column=0, padx=5)
  
    #prompts the user to enter account details
    self.login_title = ctk.CTkLabel(self.login_frame, text="Account Details", font=self.title_font)
    self.login_title.grid(row=0, column=0)
    
    self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username", width=200)
    self.username_entry.grid(row=1, column=0, padx=5, pady=10)
    self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=200)
    self.password_entry.grid(row=2, column=0, padx=5, pady=10)

    self.login_button = ctk.CTkButton(self.login_frame, text="Login", width=100)
    self.login_button.grid(row=3, column=0, padx=5, pady=5)
    self.sign_in_button = ctk.CTkButton(self.login_frame, text="Sign In", width=100)
    self.sign_in_button.grid(row=4, column=0, padx=5, pady=5)









ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Revision App")
login_page = LoginPage(root)
login_page.create_frames()
login_page.create_widgets()
root.mainloop()

