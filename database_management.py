import sqlite3

connection = sqlite3.connect("revision_app.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS stats(
                  username TEXT PRIMARY KEY,
                  right_questions INTEGER,
                  wrong_questions INTEGER,
                  FOREIGN KEY (username) REFERENCES users (username)
                  ON DELETE CASCADE
                  ON UPDATE CASCADE)"""

create_table2 = """CREATE TABLE IF NOT EXISTS users(
                  username TEXT PRIMARY KEY,
                  password TEXT)"""

cursor.execute(create_table2)
cursor.execute(create_table)

many_customers = [('Wes', 'Brown'),
                  ( 'Steph', 'Kuewa'),
                  ( 'Dan', 'Pas')]

many_customers2 = [('Wes', 0, 0),
                   ('Steph', 0, 0),
                   ('Dan', 0, 0)]


#cursor.executemany("INSERT INTO users VALUES (?, ?)", many_customers)
#cursor.executemany("INSERT INTO stats VALUES (?, ?, ?)", many_customers2)
items = cursor.execute("SELECT * FROM stats").fetchall()
#cursor.execute("DELETE FROM users WHERE username = 'Dan'")
for item in items:
  print(item)





connection.commit()
connection.close()