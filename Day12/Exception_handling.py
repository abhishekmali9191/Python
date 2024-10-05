# Exception Handling

try:
    conn = sql.connect('school1.db')

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
    # cursor.execute("DROP TABLE courses")
    # cursor.execute("DROP TABLE students")
    cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Alice', 18, 'A')")
    cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Bob', 17, 'B')")
    cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Charlie', 19, 'A')")
    cursor.execute("INSERT INTO students (name, age, grade) VALUES ('David', 18, 'B')")
    cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Eve', 17, 'A')")

    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('Math', 'Dr. Smith')")
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('Science', 'Prof. Johnson')")
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('History', 'Dr. Brown')")

    conn.commit()
    cursor.execute("SELECT * FROM students WHERE grade = 'A'")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM courses order by course_name")
    print(cursor.fetchall())
except Exception as e:
    print(e)
else:
    print()
finally:
    cursor.close()
    conn.close()
    
    
#     ###############################################################
#     OUTPUT
#     [(1, 'Alice', 18, 'A'), (3, 'Charlie', 19, 'A'), (5, 'Eve', 17, 'A')]
# [(3, 'History', 'Dr. Brown'), (1, 'Math', 'Dr. Smith'), (2, 'Science', 'Prof. Johnson')]
