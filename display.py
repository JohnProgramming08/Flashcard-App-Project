import customtkinter as ctk


class Page(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(parent)
    self.title_font = ctk.CTkFont(family="Roboto", size=20, weight="bold", underline=True)
    self.heading_font = ctk.CTkFont(family="arial", size=14, weight="bold")
    self.normal_font = ctk.CTkFont(family="arial", size=13)
    self.subheading_font = ctk.CTkFont(family="arial", size=13, underline=True)

  # Create all frames needed
  def create_frames(self):
    pass

  # Creates all widgets needed
  def create_widgets(self):
    pass

  # Change to the specified page
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
    self.information_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")
    self.login_frame = ctk.CTkFrame(self)
    self.login_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")
    self.contact_frame = ctk.CTkFrame(self)
    self.contact_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

  def create_widgets(self):
    # Explain the apps purpose
    self.title = ctk.CTkLabel(self.information_frame, text="Information", font=self.title_font)
    self.title.grid(row=0, column=0)

    self.purpose = ctk.CTkLabel(self.information_frame, text="This is a revision app to help UK students revise.\n", font=self.heading_font)
    self.purpose.grid(row=1, column=0, padx=5)
    self.purpose2 = ctk.CTkLabel(self.information_frame, text="This app has a spaced repetition algorithm, nearly\na hundred questions and more! This app was made as a holiday\nproject to improve my skills over the summer. If you would wish to\ntry it out then please press sign up!", font=self.normal_font)
    self.purpose2.grid(row=2, column=0, padx=5)

    self.contact_title = ctk.CTkLabel(self.contact_frame, text="Contact", font=self.title_font)
    self.contact_title.grid(row=0, column=0)
    self.contact_purpose = ctk.CTkLabel(self.contact_frame, text="If you have any questions or concerns please contact me at: dylan08code@gmail.com", font=self.heading_font)
    self.contact_purpose.grid(row=1, column=0, padx=5)

    # Create the login/sign up interface
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
    self.recommended_topics = []
    self.wrong = wrong
    self.right = right
    self.total_answered = wrong + right
    self.xp = xp
    
    # Avoid division by zero error
    if self.total_answered == 0:
      self.percentage_right = 0
      
    else:
      self.percentage_right = int((right / self.total_answered) * 100)
      
    self.create_frames()
    self.create_widgets()

  def create_frames(self):
    self.stats_frame = ctk.CTkFrame(self)
    self.stats_frame.grid(row=1, column=0, padx=20, pady=20, sticky="n")
    self.recommended_topics_frame = ctk.CTkFrame(self)
    self.recommended_topics_frame.grid(row=1, column=2, padx=20, pady=20, sticky="n")

  def create_widgets(self):
    # Display the users stats
    self.stats_title = ctk.CTkLabel(self.stats_frame, text="Stats", font=self.heading_font)
    self.stats_title.grid(row=0, column=0)
    self.topics_title = ctk.CTkLabel(self.recommended_topics_frame, text="Recommended Topics", font=self.heading_font)
    self.topics_title.grid(row=0, column=0)
      
    self.update_button = ctk.CTkButton(self.stats_frame, text="Update Stats", width=100, command=self.update_stats)
    self.update_button.grid(row=5, column=0, padx=5, pady=5)
    
    self.questions_answered = ctk.CTkLabel(self.stats_frame, text=f"Questions answered: {self.right + self.wrong}", font=self.normal_font)
    self.questions_answered.grid(row=2, column=0)
    self.percentage_display = ctk.CTkLabel(self.stats_frame, text=f"Percentage right: {self.percentage_right}%", font=self.normal_font)
    self.percentage_display.grid(row=3, column=0)
    self.xp_display = ctk.CTkLabel(self.stats_frame, text=f"XP: {self.xp}", font=self.normal_font)
    self.xp_display.grid(row=4, column=0)

    self.recommended_topics_label = ctk.CTkLabel(self.recommended_topics_frame, text="", font=self.normal_font)
    self.recommended_topics_label.grid(row=1, column=0, padx=5, pady=5)
    
  def update_stats(self):
    self.questions_answered.configure(text=f"Questions answered: {self.total_answered}")
    self.percentage_display.configure(text=f"Percentage right: {self.percentage_right}%")
    self.xp_display.configure(text=f"XP: {self.xp}")
  

class TopicsPage(Page):
  def __init__(self, parent):
    super().__init__(parent)
    self.create_frames()
    self.create_widgets()

  def create_frames(self):
    self.topics_frame = ctk.CTkFrame(self)
    self.topics_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")
    self.subtopics_frame = ctk.CTkFrame(self)
    self.subtopics_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")
    self.chosen_topics_frame = ctk.CTkFrame(self)
    self.chosen_topics_frame.grid(row=0, column=2, padx=20, pady=20, sticky="n")

  def create_widgets(self):
    self.topics_title = ctk.CTkLabel(self.topics_frame, text="Topics", font=self.title_font)
    self.topics_title.grid(row=0, column=0)
    
    # Display all topics as radio buttons and all subtopics as checkboxes
    self.topics = [["1.1 Systems architecture", "1.1.1 CPU architecture", "1.1.2 CPU performance", "1.1.3 Embedded systems"],
                   ["1.2 Memory and storage", "1.2.1 Primary storage", "1.2.2 Secondary storage", "1.2.3 Units of storage", "1.2.4 Data storage", "1.2.5 Compression"],
                   ["1.3 Networks and protocols", "1.3.1 Networks and topologies", "1.3.2 Networks, protocols and layers"],
                   ["1.4 Network security", "1.4.1 Threats to computer systems", "1.4.2 Identifying and preventing vulnerabilities"],
                   ["1.5 Systems software", "1.5.1 Operating systems", "1.5.2 Utility software"],
                   ["1.6 Impacts of technology", "1.6.1 Impacts of technology"],
                   ["2.1 Algorithms", "2.1.1 Computational thinking", "2.1.2 Designing algorithms", "2.1.3 Searching and sorting algorithms"],
                   ["2.2 Programming fundamentals", "2.2.1 Programming fundamentals", "2.2.2 Data types", "2.2.3 Programming techniques"],
                   ["2.3 Robust programs", "2.3.1 Defensive design", "2.3.2 Testing"],
                   ["2.4 Boolean logic", "2.4.1 Boolean logic"],
                   ["2.5 Languages and IDEs", "2.5.1 Languages", "2.5.1 IDEs"]]

    self.selected_topics = []
    # Make a list of checked subtopics
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
    
    # Create a checkbox for each subtopic
    self.subtopics_title = ctk.CTkLabel(self.subtopics_frame, text="Subtopics", font=self.subheading_font)
    self.subtopics_title.grid(row=0, column=0)

    self.checked_topic = ctk.StringVar(value="off")
    self.subtopic_buttons = []
    def display_subtopics():
      # Destroy current checkboxes before creating new ones
      for subtopic in reversed(self.subtopic_buttons):
        subtopic_index = self.subtopic_buttons.index(subtopic)
        self.subtopic_buttons.pop(subtopic_index)
        self.selected_topics.clear()
        subtopic.destroy()

      # Create new checkboxes
      # Self.topics is an array of arrays (topic name, then subtopics)
      for i in range(len(self.topics[self.topic_number.get()])-1):
        topic_number = self.topics[self.topic_number.get()]
        subtopic = topic_number[i+1]  # First element isn't a subtopic
        subtopic_button = ctk.CTkCheckBox(self.subtopics_frame, text=subtopic, font=self.normal_font, variable=ctk.StringVar(value="off"), onvalue="on", offvalue="off", command=lambda s=subtopic: checkbox_command(s))
        subtopic_button.grid(row=i+1, column=0, sticky="w")
        self.subtopic_buttons.append(subtopic_button)
        
    # Display all topics as radio buttons 
    self.topic_number = ctk.IntVar(value=0)
    for topic in self.topics:
      topic_button = ctk.CTkRadioButton(self.topics_frame, text=topic[0], font=self.heading_font, value=self.topics.index(topic), variable=self.topic_number, command=display_subtopics)
      topic_button.grid(row=self.topics.index(topic) + 1, column=0, sticky="w")
  
    self.add_button = ctk.CTkButton(self, text="Add", fg_color="green")
    self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
    self.remove_button = ctk.CTkButton(self, text="Remove", fg_color="red")
    self.remove_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
  
    # Display chosen topics
    self.chosen_topics_title = ctk.CTkLabel(self.chosen_topics_frame, text="Chosen Topics", font=self.title_font)
    self.chosen_topics_title.grid(row=0, column=0)
    self.chosen_topics = ctk.CTkLabel(self.chosen_topics_frame, text="", font=self.normal_font)
    self.chosen_topics.grid(row=1, column=0)


class StudyPage(Page):
  def __init__(self, parent):
    super().__init__(parent)
    self.questions = []
    self.delayed_questions = []
    self.create_frames()
    self.create_widgets()
    self.original_colour = self.flashcard_frame.cget("fg_color")
    self.index = 0

  def create_frames(self):
    self.flashcard_frame = ctk.CTkFrame(self, width=300, height=200)

  def create_widgets(self):
    self.question = ctk.CTkLabel(self.flashcard_frame, text="")
    self.answer = ctk.CTkLabel(self.flashcard_frame, text="")
      
    self.study_button = ctk.CTkButton(self, text="Get Studying!", command=lambda: self.start_study())
    self.study_button.grid(row=0, column=0, pady=100, padx=150)
    
    def show_answer():
      answer = self.questions[self.index][1]
      self.answer.configure(text=f"Answer:\n{answer}", font=self.normal_font)
      self.correct_button.grid(row=2, column=0, padx=5, pady=10)
      self.incorrect_button.grid(row=2, column=2, padx=5, pady=10)
      self.answer_button.grid_forget()

    self.answer_button = ctk.CTkButton(self.flashcard_frame, text="Show Answer", command=show_answer)
    self.correct_button = ctk.CTkButton(self.flashcard_frame, text="Correct", fg_color="green", command=lambda: self.question_state("green"))
    self.incorrect_button = ctk.CTkButton(self.flashcard_frame, text="Incorrect", fg_color="red", command=lambda: self.question_state("red"))

    # Display the next question in the array
    def next_question():
      try:
        question = self.questions[self.index][0]
        self.flashcard_frame.configure(fg_color=self.original_colour)
        self.question.configure(text=f"Question:\n{question}", font=self.normal_font)
        self.answer.configure(text="")
        self.answer_button.grid(row=2, column=1, padx=5, pady=10)
        self.next_button.grid_forget()

      # Use recursion to display the next question if the current one is delayed
      except IndexError:
        self.delayed_questions = self.merge_sort(self.delayed_questions)
        question = self.delayed_questions[0]
        self.questions.insert(1, question)
        self.delayed_questions.pop(0)
        self.index = 0
        next_question()

    self.next_button = ctk.CTkButton(self.flashcard_frame, text="Next Question", command=next_question)

    # Return page to original state
    def stop_study():
      self.flashcard_frame.configure(fg_color=self.original_colour)
      self.flashcard_frame.grid_forget()
      self.question.grid_forget()
      self.answer.grid_forget()
      self.answer_button.grid_forget()
      self.next_button.grid_forget()
      self.correct_button.grid_forget()
      self.stop_button.grid_forget()
      self.study_button.grid(row=0, column=0, pady=100, padx=150)
      
    self.stop_button = ctk.CTkButton(self, text="Stop Studying", command=stop_study)

  # Some functions are defined outside of create_widgets due to being called in main.py
  # Set up flashcard UI and functionality
  def start_study(self):
    try:
      self.study_button.grid_forget()
      self.flashcard_frame.grid(row=0, column=0, padx=20, pady=20)
      self.question.configure(text=f"Question:\n{self.questions[self.index][0]}", font=self.normal_font)
      self.question.grid(row=0, column=1, padx=10, pady=10)
      self.answer.configure(text="")
      self.answer.grid(row=1, column=1, padx=10, pady=10)
      self.answer_button.grid(row=2, column=1, padx=20, pady=20)
      self.stop_button.grid(row=1, column=0, padx=10, pady=10)

    # Use recursion to display the question if the current one is delayed
    except IndexError:
      if len(self.delayed_questions) == 0:
        self.flashcard_frame.grid_forget()
        self.study_button.grid(row=0, column=0, pady=100, padx=150)

      else:
        self.delayed_questions = self.merge_sort(self.delayed_questions)
        self.questions.append(self.delayed_questions[0])
        self.delayed_questions.pop(0)
        self.index = 0
        self.start_study()

  def question_state(self, colour):
    self.next_button.grid(row=2, column=1, padx=5, pady=10)
    self.flashcard_frame.configure(fg_color=colour)
    self.correct_button.grid_forget()
    self.incorrect_button.grid_forget()

  def merge_sort(self, array):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(array) > 1:
      midpoint = len(array) // 2

      # Split the array into left and right halves and recursively sort them
      left_half = array[:midpoint]
      right_half = array[midpoint:]
      self.merge_sort(left_half)
      self.merge_sort(right_half)

      # Merge the sorted halves back into the original array based on delay values
      i = j = k = 0
      while i < len(left_half) and j < len(right_half):
        if left_half[i][4] < right_half[j][4]:
          array[k] = left_half[i]
          i += 1
        else:
          array[k] = right_half[j]
          j += 1
        k += 1

      # If there are any remaining elements in the left half, add them
      while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1

      # If there are any remaining elements in the right half, add them
      while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

    return array
    
    
class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Revision App")
    self.intro_page = IntroPage(self, "")
    self.intro_page.pack()

    # Create the other pages but don't add them
    self.tabs = ctk.CTkTabview(self)
    self.home_tab = self.tabs.add("Home")
    self.home_page = HomePage(self.home_tab, wrong=5, right=4, xp=65)
    self.home_page.pack(fill='both', expand=True)

    self.topics_tab = self.tabs.add("Topics")
    self.topics_page = TopicsPage(self.topics_tab)
    self.topics_page.pack(fill='both', expand=True)

    self.study_tab = self.tabs.add("Study")
    self.study_page = StudyPage(self.study_tab)
    self.study_page.pack(fill='both', expand=True)

  def error_message(self, message):
    error_window = ctk.CTkToplevel(self, fg_color="red")
    error_window.title("Error")
    error = ctk.CTkLabel(error_window, text=message)
    error.pack()

