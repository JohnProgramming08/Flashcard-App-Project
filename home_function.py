import sqlite3





#displays topics that the user does worst on
def get_recommended_topics(username, app):
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

def update_stats1(app, get_stats):
  #updates all stats displayed to the user
  username = app.intro_page.username_entry.get()
  stats = get_stats(username)
  app.home_page.total_answered = stats[1] + stats[2]
  app.home_page.percentage_right = 0

  if (stats[1] + stats[2]) != 0:
    percentage_right = int(stats[1] / (stats[1] + stats[2]) * 100) 
    app.home_page.percentage_right = percentage_right

  app.home_page.xp = stats[3]
  app.home_page.update_stats()
  get_recommended_topics(username, app)
