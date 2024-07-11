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
    get_recommended_topics(username)
  
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

  #displays topics that the user does worst on
  def get_recommended_topics(username):
    def bubble_sort(array):
      n = len(array) 
      for i in range(n):
        #traverse the array from the beginning to n-i-1
        #the last i elements are already sorted
        for j in range(n - i - 1):
          #swap if the current element is greater than the next element
          if array[j][2] < array[j + 1][2]:
            array[j], array[j + 1] = array[j + 1], array[j]
            
      return array

    #gets all the questions and sorts them by the number of wrong answers (descending)
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM question_stats WHERE username = ?", (username,))
    questions = cursor.fetchall()
    questions = bubble_sort(questions)

    #displays the questions that the user performs worst on
    recommended_topics = []
    chosen_topics = 0
    index = 0
    while chosen_topics < 5:
      cursor.execute("SELECT subtopic FROM flashcards WHERE question_text = ?", (questions[index][1],))
      subtopic = cursor.fetchone()[0]
      if subtopic in recommended_topics:
        pass

      else:
        recommended_topics.append(subtopic)
        chosen_topics += 1

      index += 1

    recommended_topics_text = ""
    for i in recommended_topics:
      recommended_topics_text +=f"{i}\n"

    connection.close()
    app.home_page.recommended_topics_label.configure(text=recommended_topics_text)
    

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

    #adds the questions without a delay to a questions list
    for i in reversed(questions):
      delay = cursor.execute("SELECT delay FROM question_stats WHERE username = ? AND question = ?", (username, i[0]))
      delay = delay.fetchone()
      if delay[0] == 0:
        app.study_page.delayed_questions.remove(i)
        app.study_page.questions.append(i)
        
      else:
        #adds the delay to the tuple
        delayed_question = i + (delay[0],)
        app.study_page.delayed_questions[app.study_page.delayed_questions.index(i)] = delayed_question

    connection.close()
    app.study_page.start_study()

  #upates the questions delays
  def update_delayed_questions(delay, stats):
    delayed_question = app.study_page.questions[app.study_page.index]
    delayed_question = list(delayed_question)
    delayed_question.append(delay)
    app.study_page.delayed_questions.append(delayed_question)
    app.study_page.questions.pop(app.study_page.questions.index(app.study_page.questions[app.study_page.index]))
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE question_stats SET delay = ? WHERE username = ? AND question = ?", (delay, stats[0], delayed_question[0]))
    connection.commit()

    #updates the delayed_questions lists delays
    for i in app.study_page.delayed_questions:
      temp_i = i
      i = list(i)
      i[4] -= 1
      i = tuple(i)
      app.study_page.delayed_questions[app.study_page.delayed_questions.index(temp_i)] = i
      
      #updates the question_stats table
      cursor.execute("UPDATE question_stats SET delay = ? WHERE username = ? AND question = ?", (i[4], stats[0], i[0]))
      connection.commit()
      
      if i[4] == 0:
        app.study_page.delayed_questions.remove(i)
        app.study_page.questions.append(i)

    connection.close()
  
  def incorrect():
    #adds one to wrong questions and 5 to exp in stats table
    stats = list(get_stats(app.intro_page.username_entry.get()))
    stats[2] += 1
    stats[3] += 5
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE stats SET wrong_questions = ?, exp = ? WHERE username = ?", (stats[2], stats[3], stats[0]))
    connection.commit()

    #adds one to wrong questions in question_stats table
    cursor.execute("SELECT wrong_answers FROM question_stats WHERE username = ? AND question = ?", (stats[0], app.study_page.questions[app.study_page.index][0]))
    wrong_answers = cursor.fetchone()[0] + 1
    cursor.execute("UPDATE question_stats SET wrong_answers = ? WHERE username = ? AND question = ?", (wrong_answers, stats[0], app.study_page.questions[app.study_page.index][0]))
    connection.commit()
    connection.close()

    update_delayed_questions(5, stats)
    app.study_page.question_state("red")

  
  def correct():
    #adds one to right questions and 10 to exp in stats table
    stats = list(get_stats(app.intro_page.username_entry.get()))
    stats[1] += 1
    stats[3] += 10
    connection = sqlite3.connect("revision_app.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE stats SET right_questions = ?, exp = ? WHERE username = ?", (stats[1], stats[3], stats[0]))
    connection.commit()

    #adds one to right questions in question_stats table
    cursor.execute("SELECT right_answers FROM question_stats WHERE username = ? AND question = ?", (stats[0], app.study_page.questions[app.study_page.index][0]))
    right_answers = cursor.fetchone() + 1
    cursor.execute("UPDATE question_stats SET right_answers = ? WHERE username = ? AND question = ?", (right_answers, stats[0], app.study_page.questions[app.study_page.index]))
    connection.commit()
    connection.close()
    
    update_delayed_questions(10, stats)
    app.study_page.question_state("green")

  #implementing all of the back end logic into the front end
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




#MERGE SORT SEEMS TO WORK 
#IMPLEMENT IT IN THE DISPLAY PAGE