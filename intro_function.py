import sqlite3

def sign_up(username, password):
  #connect to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  #determines if the username is valid
  valid = True
  if username:
    for i in username:
      if i == " ":
        valid = False
        break

  else:
    valid = False

  #checks if the username is already taken
  if valid is True:
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    #add the user to the database
    if user is None:
      cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
      cursor.execute("INSERT INTO stats (username, right_questions, wrong_questions) VALUES (?, ?, ?)", (username, 0, 0))
      connection.commit()
      return True

    else:
      return "used"

  else:
    return "spaces"

def login(username, password):
  #connect to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
  user = cursor.fetchone()
  connection.close()
  #returns false if the details are wrong
  if user is not None:
    return True

  else:
    return False
