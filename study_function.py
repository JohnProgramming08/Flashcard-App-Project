import sqlite3

def get_questions(chosen_topics):
  #creates a connection to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  questions = []
  for i in chosen_topics:
    cursor.execute("SELECT * FROM flashcards WHERE subtopic = ?", (i,))
    for j in cursor.fetchall():
      questions.append(j)
    
    
  
  #gets the questions from the database
  #cursor.execute(f"SELECT * FROM flashcards WHERE subtopic IN {chosen_topics}")
  return questions

