import sqlite3
from display import HomePage, App
from intro_function import sign_up, login
from topics_function import Topics 
from study_function import get_questions

def main():
  #gets the users stats
  def get_stats(username):
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    user_stats = cursor.execute("SELECT * FROM stats WHERE username = ?", (username,)).fetchone()
    connection.close() 
    return user_stats

  #changes to the home page
  def show_home_page(username):
    stats = get_stats(username)
    app.home_page = HomePage(app.home_tab, stats[2], stats[1], stats[3])
    app.intro_page.change_pages(app.intro_page, app.tabs)
  
  #if the username is valid, creates new account 
  def sign_up2():
    username = app.intro_page.username_entry.get()
    password = app.intro_page.password_entry.get()
    attempt = sign_up(username, password)
    if attempt is True:
      show_home_page(username)

    #returns an appropriate error message 
    elif attempt == "used":
      app.error_message("Username already taken")

    else:
      app.error_message("Spaces are not allowed")
  
  def login2():
    #if details are valid, logs in
    username = app.intro_page.username_entry.get()
    password = app.intro_page.password_entry.get()
    if login(username, password) is True:
      show_home_page(username)

    #returns an appropriate error message
    else:
      app.error_message("Incorrect username or password")

  def show_topics(topics):
    chosen_topics = ""
    for i in topics:
      chosen_topics += f"{i}\n"
    app.topics_page.chosen_topics.configure(text=chosen_topics)

  #adds selected topics to the list
  def add_click():
    selected_topics = app.topics_page.selected_topics
    selected_topics = topics.click(selected_topics, 1)
    show_topics(selected_topics)

  #removes selected topics from the list
  def remove_click():
    selected_topics = app.topics_page.selected_topics
    selected_topics = topics.click(selected_topics, 0)
    show_topics(selected_topics)

  #gets the questions with the chosen topics from database
  def select_questions():
    questions = get_questions(app.topics_page.chosen_topics.cget("text").split("\n"))
    app.study_page.questions = questions
    app.study_page.start_study()
    
  
  app = App()
  app.intro_page.sign_up_button.configure(command=sign_up2)
  app.intro_page.login_button.configure(command=login2)
  topics = Topics()
  app.topics_page.add_button.configure(command=add_click)
  app.topics_page.remove_button.configure(command=remove_click)
  app.study_page.study_button.configure(command=select_questions)
  app.mainloop()

if __name__ == "__main__":
  main()