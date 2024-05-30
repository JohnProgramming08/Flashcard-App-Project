import sqlite3

def sign_up(username, password):
  #connect to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  #check if the username is in the database
  cursor.execute("SELECT * FROM users WHERE username=?", (username,))
  user = cursor.fetchone()
  #add the user to the database
  if user is None:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()
    #current_page.remove()
    #new_page.pack()
    return True

  else:
    return False

  


