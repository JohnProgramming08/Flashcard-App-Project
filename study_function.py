import sqlite3


def get_questions(chosen_topics):
  # Connect to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  # Return a list of all questions with chosen subtopics
  questions = []
  for topic in chosen_topics:
    cursor.execute("SELECT * FROM flashcards WHERE subtopic = ?", (topic,))
    chosen_questions = cursor.fetchall()
    for question in chosen_questions:
      questions.append(question)
    
  return questions

# Get the questions with the chosen topics from the database
def select_questions(app):
  chosen_topics = app.topics_page.chosen_topics.cget("text")
  questions = get_questions(chosen_topics.split("\n"))
  app.study_page.delayed_questions = questions
  username = app.intro_page.username_entry.get()

  # Connect to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  # Add the questions without a delay to a questions list
  for question in reversed(questions):
    question_text = question[0]
    cursor.execute("SELECT delay FROM question_stats WHERE username = ? AND question = ?", (username, question_text))
    delay = cursor.fetchone()[0]
    
    if delay == 0:
      app.study_page.delayed_questions.remove(question)
      app.study_page.questions.append(question)

    else:
      # Add the delay for the question
      delayed_question = question + (delay,)
      question_index = app.study_page.delayed_questions.index(question)
      app.study_page.delayed_questions[question_index] = delayed_question

  connection.close()
  app.study_page.start_study()

# Update the questions delays
def update_delayed_questions(delay, stats, app):
  # Add the delay to the question
  delayed_question = app.study_page.questions[app.study_page.index]
  delayed_question = list(delayed_question)
  delayed_question.append(delay)
  app.study_page.delayed_questions.append(delayed_question)
  question_index = app.study_page.questions.index(app.study_page.questions[app.study_page.index])
  app.study_page.questions.pop(question_index)

  # Update the users stats
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()
  username = stats[0]
  question_text = delayed_question[0]
  cursor.execute("UPDATE question_stats SET delay = ? WHERE username = ? AND question = ?", (delay, username, question_text))
  connection.commit()

  # Update the delayed_questions lists delays
  for question in app.study_page.delayed_questions:
    old_question = question
    question = list(question)
    question[4] -= 1  # Take 1 away from the questions delay
    question = tuple(question)
    old_question_index = app.study_page.delayed_questions.index(old_question)
    app.study_page.delayed_questions[old_question_index] = question

    # Update the question_stats table
    question_text = question[0]
    delay = question[4]
    cursor.execute("UPDATE question_stats SET delay = ? WHERE username = ? AND question = ?", (delay, username, question_text))
    connection.commit()

    if question[4] == 0:
      app.study_page.delayed_questions.remove(question)
      app.study_page.questions.append(question)

  connection.close()

def incorrect(app, get_stats):
  # Add one to wrong questions and 5 to exp in stats table
  username = app.intro_page.username_entry.get()
  stats = list(get_stats(app.intro_page.username_entry.get()))
  stats[2] += 1
  stats[3] += 5

  # Update the users stats
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()
  wrong = stats[2]
  xp = stats[3]
  cursor.execute("UPDATE stats SET wrong_questions = ?, exp = ? WHERE username = ?", (wrong, xp, username))
  connection.commit()

  # Add one to wrong questions in question_stats table
  question = app.study_page.questions[app.study_page.index][0]
  cursor.execute("SELECT wrong_answers FROM question_stats WHERE username = ? AND question = ?", (username, question))
  wrong_answers = cursor.fetchone()[0] + 1
  cursor.execute("UPDATE question_stats SET wrong_answers = ? WHERE username = ? AND question = ?", (wrong_answers, username, question))
  connection.commit()
  connection.close()

  update_delayed_questions(5, stats, app)
  app.study_page.question_state("red")

def correct(app, get_stats):
  # Add one to right questions and 10 to exp in stats table
  stats = list(get_stats(app.intro_page.username_entry.get()))
  stats[1] += 1
  stats[3] += 10

  # Update the users stats
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()
  right = stats[1]
  xp = stats[3]
  username = stats[0]
  cursor.execute("UPDATE stats SET right_questions = ?, exp = ? WHERE username = ?", (right, xp, username))
  connection.commit()

  # Add one to right questions in question_stats table
  question = app.study_page.questions[app.study_page.index][0]
  cursor.execute("SELECT right_answers FROM question_stats WHERE username = ? AND question = ?", (username, question))
  right_answers = cursor.fetchone()[0] + 1
  cursor.execute("UPDATE question_stats SET right_answers = ? WHERE username = ? AND question = ?", (right_answers, username, question))
  connection.commit()
  connection.close()

  update_delayed_questions(10, stats, app)
  app.study_page.question_state("green")




