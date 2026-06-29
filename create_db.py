import sqlite3

# Create a new database file
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create a table named 'users'
c.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    otp TEXT
)''')

conn.commit()
conn.close()

print("✅ Database and users table created successfully!")
