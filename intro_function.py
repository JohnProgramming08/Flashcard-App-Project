import sqlite3


# Change to the home page
def show_home_page(username, update_stats2, get_stats, get_recommended_topics, app):
  update_stats2(app, get_stats)
  app.intro_page.change_pages(app.intro_page, app.tabs)
  get_recommended_topics(username, app)

# Add the users data to the database
def sign_up(username, password, update_stats2, get_stats, get_recommended_topics, app):
  username = app.intro_page.username_entry.get()
  password = app.intro_page.password_entry.get()
  
  # Connect to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  # Determine if the username is valid
  valid = True
  if username:
    for character in username:
      if character == " " or character == '"':
        app.error_message("Spaces and quotation marks are not allowed")
        valid = False
        break

  else:
    app.error_message("You must have a username")
    valid = False

  # Check if the username is already taken
  if valid is True:
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    
    # Add the user to the database if they aren't already in it 
    if user is None:
      
      cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
      cursor.execute("INSERT INTO stats (username, right_questions, wrong_questions, exp) VALUES (?, ?, ?, ?)", (username, 0, 0, 0))
      connection.commit()

      # Add the users stats to the database for each question
      cursor.execute("SELECT * FROM flashcards")
      questions = cursor.fetchall()

      def add_question(question):
        cursor.execute("INSERT INTO question_stats (username, question, wrong_answers, right_answers, delay) VALUES (?, ?, ?, ?, ?)", (username, question, 0, 0, 0))
        connection.commit()
          
      for question in questions:
        question = list(question)
        add_question(question[0])

      show_home_page(username, update_stats2, get_stats, get_recommended_topics, app)
      
    else:
      app.error_message("Username is already in use")

def login(update_stats2, get_stats, get_recommended_topics, app):
  username = app.intro_page.username_entry.get()
  password = app.intro_page.password_entry.get()
  
  # Connect to the database
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()

  cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
  user = cursor.fetchone()
  connection.close()
  
  # Display an error if the login details are wrong
  if user:
    show_home_page(username, update_stats2, get_stats, get_recommended_topics, app)

  else:
    app.error_message("Incorrect username or password")

