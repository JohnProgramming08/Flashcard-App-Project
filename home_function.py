import sqlite3


# Display topics that the user does worst on
def get_recommended_topics(username, app):
  def bubble_sort(array):
    length = len(array) 
    for i in range(length):
      # The last i elements are already sorted
      for j in range(length - i - 1):
        # Swap if the current element is less than the next element
        if array[j][2] < array[j + 1][2]:
          array[j], array[j + 1] = array[j + 1], array[j]

    return array

  # Get all the questions and sort them by the number of wrong answers (descending)
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM question_stats WHERE username = ?", (username,))
  questions = cursor.fetchall()
  questions = bubble_sort(questions)

  # Display the 5 topics that the user performs worst on
  recommended_topics = []
  chosen_topics = 0
  index = 0
  while chosen_topics < 5:
    question = questions[index][1]
    cursor.execute("SELECT subtopic FROM flashcards WHERE question_text = ?", (question,))
    subtopic = cursor.fetchone()[0]
    # Only Add the subtopic if it is not already in the list
    if subtopic not in recommended_topics:
      recommended_topics.append(subtopic)
      chosen_topics += 1

    index += 1

  recommended_topics_text = ""
  for topic in recommended_topics:
    recommended_topics_text +=f"{topic}\n"

  connection.close()
  app.home_page.recommended_topics_label.configure(text=recommended_topics_text)

# Update all stats displayed to the user
def update_stats2(app, get_stats):
  username = app.intro_page.username_entry.get()
  stats = get_stats(username)
  right = stats[1]
  wrong = stats[2]
  total_answered = right + wrong
  app.home_page.total_answered = total_answered
  app.home_page.percentage_right = 0

  # Avoid dividing by 0
  if (right + wrong) != 0:
    percentage_right = int(right / total_answered * 100) 
    app.home_page.percentage_right = percentage_right

  app.home_page.xp = stats[3]
  app.home_page.update_stats()
  get_recommended_topics(username, app)
