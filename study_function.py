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






