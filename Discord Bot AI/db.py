import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    username TEXT
)
''')
conn.commit()

def add_user(user):
    cursor.execute('INSERT OR IGNORE INTO users (id, username) VALUES (?, ?)', (str(user.id), user.name))
    conn.commit()
