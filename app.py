import sqlite3

# Connect to SQLite's in-memory database.
# ":memory:" is a special name used for in-memory databases in SQLite.
conn = sqlite3.connect(':memory:')

# Get a cursor object.
cursor = conn.cursor()

# Create a table.
cursor.execute("""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE
    )
""")

# Insert some data.
cursor.execute("""
    INSERT INTO users(name, email) 
    VALUES 
        ('John Doe', 'john@example.com'),
        ('Jane Doe', 'jane@example.com')
""")

# Commit the transaction.
conn.commit()

# Query the data.
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Close the connection.
conn.close()
