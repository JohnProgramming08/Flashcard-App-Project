import sqlite3

def sign_up(username, password):
  #connect to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  #check if the username is valid
  valid = True
  for i in username:
    if i == "" or i == " ":
      valid = False

  #checks if the username is already taken
  if valid == True:
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    #add the user to the database
    if user is None:
      cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
      connection.commit()
      return True

    else:
      return "used"

  else:
    return "spaces"


