import customtkinter as ctk

class Page(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(parent)
    self.title_font = ctk.CTkFont(family="Roboto", size=20, weight="bold", underline=True)
    self.heading_font = ctk.CTkFont(family="arial", size=14, weight="bold")
    self.normal_font = ctk.CTkFont(family="arial", size=13)
    self.subheading_font = ctk.CTkFont(family="arial", size=13, underline=True)

  #creates all frames needed
  def create_frames(self):
    pass

  #creates and all widgets needed
  def create_widgets(self):
    pass

  #changes to the specified page
  def change_pages(self, current_page, next_page):
    current_page.pack_forget()
    next_page.pack(fill='both', expand=True)


class IntroPage(Page):
  def __init__(self, parent, sign_up):
    super().__init__(parent)
    self.sign_up = sign_up
    self.create_frames()
    self.create_widgets()

  def create_frames(self):
    self.information_frame = ctk.CTkFrame(self)
    self.information_frame.grid(row=0, column=0, padx=20, pady=20)
    self.login_frame = ctk.CTkFrame(self)
    self.login_frame.grid(row=0, column=1, padx=20, pady=20)
    self.contact_frame = ctk.CTkFrame(self)
    self.contact_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

  def create_widgets(self):
    #explains the apps purpose
    self.title = ctk.CTkLabel(self.information_frame, text="Information", font=self.title_font)
    self.title.grid(row=0, column=0)

    self.purpose = ctk.CTkLabel(self.information_frame, text="This is a revision/study app to help UK students revise.\n", font=self.heading_font)
    self.purpose.grid(row=1, column=0, padx=5)
    self.purpose2 = ctk.CTkLabel(self.information_frame, text="This app has spaced repetition algorithms, downloadable\npast papers, quizzes and more! If you would wish to try\nit out then please press sign in.", font=self.normal_font)
    self.purpose2.grid(row=2, column=0, padx=5)

    self.contact_title = ctk.CTkLabel(self.contact_frame, text="Contact", font=self.title_font)
    self.contact_title.grid(row=0, column=0)
    self.contact_purpose = ctk.CTkLabel(self.contact_frame, text="If you have any questions or concerns please contact me at: dylan08code.gmail.com", font=self.heading_font)
    self.contact_purpose.grid(row=1, column=0, padx=5)

    #login/sign up interface
    self.login_title = ctk.CTkLabel(self.login_frame, text="Account Details", font=self.title_font)
    self.login_title.grid(row=0, column=0)
    
    self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username", width=200)
    self.username_entry.grid(row=1, column=0, padx=5, pady=10)
    self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=200)
    self.password_entry.grid(row=2, column=0, padx=5, pady=10)

    self.login_button = ctk.CTkButton(self.login_frame, text="Login", width=100)
    self.login_button.grid(row=3, column=0, padx=5, pady=5)
    self.sign_up_button = ctk.CTkButton(self.login_frame, text="Sign Up", command=self.sign_up, width=100)
    self.sign_up_button.grid(row=4, column=0, padx=5, pady=5)


class HomePage(Page):
  def __init__(self, parent, wrong, right, xp):
    super().__init__(parent)
    self.wrong = wrong
    self.right = right
    self.total_answered = wrong + right
    #to avoid division by zero error
    if self.total_answered == 0:
      self.percentage_right = 0
    else:
      self.percentage_right = int((right / self.total_answered) * 100)
      self.xp = xp
    self.create_frames()
    self.create_widgets()

  def create_frames(self):
    self.stats_frame = ctk.CTkFrame(self)
    self.stats_frame.grid(row=1, column=0, padx=20, pady=20)
    self.schedule_frame = ctk.CTkFrame(self)
    self.schedule_frame.grid(row=1, column=1, padx=20, pady=20)

  def create_widgets(self):
    #displays user stats
    self.stats_title = ctk.CTkLabel(self.stats_frame, text="Stats", font=self.heading_font)
    self.stats_title.grid(row=0, column=0)
    self.schedule_title = ctk.CTkLabel(self.schedule_frame, text="Revision Schedule", font=self.heading_font)
    self.schedule_title.grid(row=0, column=0)

    self.questions_answered = ctk.CTkLabel(self.stats_frame, text=f"Questions answered: {self.right + self.wrong}", font=self.normal_font)
    self.questions_answered.grid(row=2, column=0)
    self.percentage_display = ctk.CTkLabel(self.stats_frame, text=f"Percentage right: {self.percentage_right}%", font=self.normal_font)
    self.percentage_display.grid(row=3, column=0)
    self.xp_display = ctk.CTkLabel(self.stats_frame, text=f"XP: {self.xp}", font=self.normal_font)
    self.xp_display.grid(row=4, column=0)


class TopicsPage(Page):
  def __init__(self, parent):
    super().__init__(parent)
    self.create_frames()
    self.create_widgets()

  def create_frames(self):
    self.topics_frame = ctk.CTkFrame(self)
    self.topics_frame.grid(row=0, column=0, padx=20, pady=20)
    self.subtopics_frame = ctk.CTkFrame(self)
    self.subtopics_frame.grid(row=0, column=1, padx=20, pady=20)

  def create_widgets(self):
    self.topics_title = ctk.CTkLabel(self.topics_frame, text="Topics", font=self.title_font)
    self.topics_title.grid(row=0, column=0)

    self.topics = ["1.1 Systems architecture",
                   "1.2 Memory and storage",
                   "1.3 Networks and protocols",
                   "1.4 Network security",
                   "1.5 Systems software",
                   "1.6 Impacts of technology",
                   "2.1 Algorithms",
                   "2.2 Programming fundamentals",
                   "2.3 Robust programs",
                   "2.4 Boolean logic",
                   "2.5 Languages and IDEs"]
    self.topic_number = ctk.IntVar(value=0)

    self.subtopics = [["1.1.1 CPU architecture", "1.1.2 CPU performance", "1.1.3 Embedded systems"],
                      ["1.2.1 Primary storage", "1.2.2 Secondary storage", "1.2.3 Units of storage", "1.2.4 Data storage", "1.2.5 Compression"],
                      ["1.3.1 Networks and topologies", "1.3.2 Networks, protocols and layers"],
                      ["1.4.1 Threats to computer systems", "1.4.2 Identifying and preventing vulnerabilities"],
                      ["1.5.1 Operating systems", "1.5.2 Utility software"],
                      ["1.6.1 Impacts of technology"],
                      ["2.1.1 Computational thinking", "2.1.2 Designing algorithms", "2.1.3 Searching and sorting algorithms"],
                      ["2.2.1 Programming fundamentals", "2.2.2 Data types", "2.2.3 Programming techniques"],
                      ["2.3.1 Defensive design", "2.3.2 Testing"],
                      ["2.4.1 Boolean logic"],
                      ["2.5.1 Languages", "2.5.1 IDEs"]]

    self.selected_topics = []
    #function to make a list of chosen subtopics
    def checkbox_command(subtopic):
      current_state = self.checked_topic.get()
      if current_state == "on":
        self.checked_topic.set("off")
        
      else:
        self.checked_topic.set("on")
        
      if subtopic in self.selected_topics:
        self.selected_topics.remove(subtopic)
        
      else:
        self.selected_topics.append(subtopic)
  
    
    #checkbox for each subtopic
    self.subtopics_title = ctk.CTkLabel(self.subtopics_frame, text="Subtopics", font=self.subheading_font)
    self.subtopics_title.grid(row=0, column=0)
    
    self.checked_topic = ctk.StringVar(value="off")
    self.subtopic_buttons = []
    def display_subtopics():
      for i in reversed(self.subtopic_buttons):
        self.subtopic_buttons.pop(self.subtopic_buttons.index(i))
        self.selected_topics.clear()
        i.destroy()
        
      for i in range(len(self.subtopics[self.topic_number.get()])):
        subtopic = self.subtopics[self.topic_number.get()][i]
        subtopic_button = ctk.CTkCheckBox(self.subtopics_frame, text=self.subtopics[self.topic_number.get()][i], font=self.normal_font, variable=ctk.StringVar(value="off"), onvalue="on", offvalue="off", command=lambda s=subtopic: checkbox_command(s))
        subtopic_button.grid(row=i+1, column=0, sticky="w")
        self.subtopic_buttons.append(subtopic_button)
        
    #displays all topics as radio buttons 
    for i in self.topics:
      topic_button = ctk.CTkRadioButton(self.topics_frame, text=i, font=self.heading_font, value=self.topics.index(i), variable=self.topic_number, command=display_subtopics)
      topic_button.grid(row=self.topics.index(i) + 1, column=0, sticky="w")

    self.add_button = ctk.CTkButton(self, text="Add")
    self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
    self.remove_button = ctk.CTkButton(self, text="Remove")
    self.remove_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
    

  
      
class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Revision App")
    self.intro_page = IntroPage(self, "")
    self.intro_page.pack()

    #creates the other pages but doesn't add them
    self.tabs = ctk.CTkTabview(self)
    self.home_tab = self.tabs.add("Home")
    self.home_page = HomePage(self.home_tab, wrong=5, right=4, xp=65)
    self.home_page.pack(fill='both', expand=True)

    self.topics_tab = self.tabs.add("Topics")
    self.topics_page = TopicsPage(self.topics_tab)
    self.topics_page.pack(fill='both', expand=True)

  def error_message(self, message):
    error_window = ctk.CTkToplevel(self, fg_color="red")
    error_window.title("Error")
    error = ctk.CTkLabel(error_window, text=message)
    error.pack()
    
  #testing purposes
  def show_login_page(self):
    self.intro_page = IntroPage(self, self.show_home_page)
    self.intro_page.pack(fill='both', expand=True)

  def show_home_page(self):
    self.intro_page.pack_forget()
    self.home_page.pack(fill='both', expand=True)


