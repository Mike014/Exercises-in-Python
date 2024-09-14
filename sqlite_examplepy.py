import sqlite3

# 3. Connecting to the Database
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# 4. Using the Cursor
# Create a cursor object
cursor = conn.cursor()

# 5. Creating Tables
# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    position TEXT NOT NULL
)
''')

# 6. Inserting Data
# Insert data into the table
cursor.execute('''
INSERT INTO workers (name, age, position)
VALUES ('John', 30, 'Developer')
''')

# Insert multiple rows at once
workers = [
    ('Jane', 28, 'Designer'),
    ('Dave', 35, 'Manager')
]
cursor.executemany('''
INSERT INTO workers (name, age, position)
VALUES (?, ?, ?)
''', workers)

# 9. Committing Changes
# Commit the changes
conn.commit()

# 7. Retrieving Data
# Retrieve data from the table
cursor.execute('SELECT * FROM workers')
all_workers = cursor.fetchall()

# 8. Analyzing Data with Loops
# Print the data
for worker in all_workers:
    print(worker)

# Retrieve a single row
cursor.execute('SELECT * FROM workers WHERE name = ?', ('John',))
john = cursor.fetchone()
print(john)

# Retrieve multiple rows
cursor.execute('SELECT * FROM workers')
some_workers = cursor.fetchmany(2)
print(some_workers)

# 10. Closing the Connection
# Close the connection
conn.close()
