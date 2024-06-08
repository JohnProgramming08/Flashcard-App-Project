import sqlite3

#create a connection to the database
connection = sqlite3.connect("revision_app.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

#create tables
create_table = """CREATE TABLE IF NOT EXISTS stats(
                  username TEXT PRIMARY KEY,
                  right_questions INTEGER,
                  wrong_questions INTEGER,
                  exp INTEGER,
                  FOREIGN KEY (username) REFERENCES users (username)
                  ON DELETE CASCADE
                  ON UPDATE CASCADE)"""

create_table2 = """CREATE TABLE IF NOT EXISTS users(
                   username TEXT PRIMARY KEY,
                   password TEXT)"""

cursor.execute(create_table2)
cursor.execute(create_table)

#insert data into tables
many_customers = [('Wes', 'Brown'),
                  ('Steph', 'Kuewa'),
                  ('Dan', 'Pas')]

many_customers2 = [('Wes', 0, 0, 0),
                   ('Steph', 0, 0, 0),
                   ('Dan', 0, 0, 0)]

cursor.executemany("INSERT INTO users VALUES (?, ?)", many_customers)
cursor.executemany("INSERT INTO stats VALUES (?, ?, ?, ?)", many_customers2)
connection.commit()

#fetch and print stats before deletion
items = cursor.execute("SELECT * FROM stats").fetchall()
for item in items:
  print(item)

#delete a user
cursor.execute("DELETE FROM users WHERE username = 'Dan'")
connection.commit()

#fetch and print stats after deletion
items = cursor.execute("SELECT * FROM stats").fetchall()
for item in items:
  print(item)
                  
#function to get stats for a user
def get_stats(username):
  connection = sqlite3.connect("revision_app.db")
  cursor = connection.cursor()
  user_stats = cursor.execute("SELECT * FROM stats WHERE username = ?", (username,)).fetchone()
  connection.close() 
  return user_stats

#get stats for 'Wes'
get_stats('Wes')

#close the initial connection
connection.close()