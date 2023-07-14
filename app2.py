import sqlite3

# Connect to SQLite's in-memory database.
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

# Create a new database on disk.
conn_disk = sqlite3.connect('my_database.db')

# Backup the in-memory database to the disk database.
conn.backup(conn_disk)

# Close both connections.
conn_disk.close()
conn.close()
