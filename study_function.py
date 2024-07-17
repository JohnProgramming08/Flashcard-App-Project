import sqlite3

def get_questions(chosen_topics):
  #creates a connection to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  #returns a list of all questions with those subtopics
  questions = []
  for i in chosen_topics:
    cursor.execute("SELECT * FROM flashcards WHERE subtopic = ?", (i,))
    for j in cursor.fetchall():
      questions.append(j)
    
  return questions

#gets the questions with the chosen topics from database
def select_questions(app):
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
def update_delayed_questions(delay, stats, app):
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

def incorrect(app, get_stats):
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

  update_delayed_questions(5, stats, app)
  app.study_page.question_state("red")

def correct(app, get_stats):
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
  right_answers = cursor.fetchone()[0] + 1
  cursor.execute("UPDATE question_stats SET right_answers = ? WHERE username = ? AND question = ?", (right_answers, stats[0], app.study_page.questions[app.study_page.index][0]))
  connection.commit()
  connection.close()

  update_delayed_questions(10, stats, app)
  app.study_page.question_state("green")




