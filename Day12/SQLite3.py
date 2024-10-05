import sqlite3 as sql
# Establishing a connection
conn = sql.connect('DAIBatch2024.db')

# Creating a cursor object
cursor = conn.cursor()

# cursor.execute('''DROP TABLE IF EXISTS users''')

# create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

cursor.execute('''INSERT INTO users (name, age) VALUES ('Mayura', 30)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('Mayuresh', 25)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('Charlie', 35)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('David', 28)''')
cursor.execute('''INSERT INTO users (name, age) VALUES ('Eve', 32)''')

# Commit the changes
conn.commit()

# query with order by
cursor.execute('SELECT * FROM users ORDER BY age DESC')
result = cursor.fetchall()
for row in result:
    print(row)

while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)

#  query with group by
cursor.execute('SELECT age, COUNT(*) as count FROM users GROUP BY age')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute('UPDATE users SET age = 31 WHERE name = "Mayura"')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT * FROM users where name LIKE 'Mayura'")
result = cursor.fetchall()
for row in result:
    print(row)
print(result)
cursor.close()
conn.close()

#######################################################
# OUTPUT
# (3, 'Charlie', 35)
# (5, 'Eve', 32)
# (1, 'Mayura', 30)
# (4, 'David', 28)
# (2, 'Mayuresh', 25)
# (25, 1)
# (28, 1)
# (30, 1)
# (32, 1)
# (35, 1)
# (1, 'Mayura', 31)
# [(1, 'Mayura', 31)]