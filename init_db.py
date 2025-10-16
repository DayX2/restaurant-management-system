import sqlite3

conn = sqlite3.connect('restaurant.db')

cursor = conn.cursor()

with open('schema.sql', 'r') as f:
    schema = f.read()
    cursor.executescript(schema)

print("Database created successfully!!!")

conn.close()