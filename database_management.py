import sqlite3

#function to get stats for a user
def get_stats(username):
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()
  user_stats = cursor.execute("SELECT * FROM stats WHERE username = ?", (username,)).fetchone()
  connection.close() 
  return user_stats



