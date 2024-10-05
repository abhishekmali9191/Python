# Assignment 1
conn = sql.connect('school.db')

cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor TEXT
)
''')

cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Alice', 18, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Bob', 17, 'B')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Charlie', 19, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('David', 18, 'B')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Eve', 17, 'A')")

cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('Math', 'Dr. Smith')")
cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('Science', 'Prof. Johnson')")
cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('History', 'Dr. Brown')")

conn.commit()

print(cursor.fetchall())

cursor.execute("SELECT * FROM students WHERE grade = 'A'")

cursor.execute("SELECT * FROM courses order by course_name")

cursor.execute("UPDATE students SET grade = 'A' WHERE name = 'David'")

cursor.execute("UPDATE courses SET instructor = 'Dr. Johnson' WHERE course_id = 2")

cursor.execute("DELETE FROM students WHERE id = 4")
conn.commit()

cursor.execute("DROP TABLE courses")
cursor.execute("DROP TABLE students")
cursor.close()
conn.close()

