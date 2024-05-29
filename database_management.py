import sqlite3

connection = sqlite3.connect("revision_app.db")
cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS users(
                  username TEXT,
                  password TEXT)"""
cursor.execute(create_table)
many_customers = [('Wes', 'Brown'),
                  ( 'Steph', 'Kuewa'),
                  ( 'Dan', 'Pas')]

cursor.executemany("INSERT INTO users VALUES (?, ?)", many_customers)


connection.commit()
connection.close()