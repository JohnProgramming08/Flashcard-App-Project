import sqlite3
from display import HomePage, App
from intro_function import sign_up, login
from topics_function import Topics 
from study_function import get_questions

def main():
  #returns the users stats
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
    app.home_page.pack(fill='both', expand=True)
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

  #if details are valid, logs in
  def login2():
    username = app.intro_page.username_entry.get()
    password = app.intro_page.password_entry.get()
    if login(username, password) is True:
      show_home_page(username)

    #returns an appropriate error message
    else:
      app.error_message("Incorrect username or password")

  #displays all chosen topics
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
    app.study_page.delayed_questions = questions
    username = app.intro_page.username_entry.get()
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()

    #adds the questions with a delay to a delayed questions list
    for i in reversed(questions):
      delay = cursor.execute("SELECT delay FROM question_stats WHERE username = ? AND question = ?", (username, i[0]))
      delay = delay.fetchone()
      connection.close()
      if delay == 0:
        app.study_page.delayed_questions.remove(i)
        app.study_page.questions.append(i)
        
      else:
        #adds the delay to the tuple
        delayed_question = i + (delay,)
        app.study_page.delayed_questions[app.study_page.delayed_questions.index(i)] = delayed_question

    app.study_page.start_study()

  #upates the questions delays
  def update_delayed_questions(delay, stats):
    delayed_question = app.study_page.questions[app.study_page.index]
    delayed_question = list(delayed_question)
    delayed_question.append(delay)
    app.study_page.delayed_questions.append(delayed_question)
    app.study_page.questions.pop(app.study_page.questions.index(app.study_page.questions[app.study_page.index]))
    
    for i in app.study_page.delayed_questions:
      i[4] -= 1
      #updates the question_stats table
      connection = sqlite3.connect("revision_app.db")
      cursor = connection.cursor()
      cursor.execute("UPDATE question_stats SET delay = ? WHERE username = ? AND question = ?", (delay, stats[0], i[0]))
      connection.commit()
      connection.close()
      
      if i[4] == 0:
        app.study_page.delayed_questions.remove(i)
        app.study_page.questions.append(i)
  
  #adds one to wrong questions and 5 to exp and updates the question_stats table
  def incorrect():
    stats = list(get_stats(app.intro_page.username_entry.get()))
    stats[2] += 1
    stats[3] += 5
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE stats SET wrong_questions = ?, exp = ? WHERE username = ?", (stats[2], stats[3], stats[0]))
    connection.commit()
    connection.close()
    update_delayed_questions(5, stats)
    app.study_page.question_state("red")

  #adds one to right questions and 10 to exp and updates the question_stats table
  def correct():
    stats = list(get_stats(app.intro_page.username_entry.get()))
    stats[1] += 1
    stats[3] += 10
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE stats SET wrong_questions = ?, exp = ? WHERE username = ?", (stats[1], stats[3], stats[0]))
    connection.commit()
    connection.close()
    update_delayed_questions(10, stats)
    app.study_page.question_state("green")
  
  app = App()
  app.intro_page.sign_up_button.configure(command=sign_up2)
  app.intro_page.login_button.configure(command=login2)
  topics = Topics()
  app.topics_page.add_button.configure(command=add_click)
  app.topics_page.remove_button.configure(command=remove_click)
  app.study_page.study_button.configure(command=select_questions)
  app.study_page.incorrect_button.configure(command=incorrect)
  app.study_page.correct_button.configure(command=correct)
  app.mainloop()

if __name__ == "__main__":
  main()