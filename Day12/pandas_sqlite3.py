import sqlite3 as sql
import pandas as pd
try:
    conn = sql.connect('company.db')
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        dept_id INTEGER PRIMARY KEY,
        dept_name TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY,
        emp_name TEXT NOT NULL,
        dept_id INTEGER,
        FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
    )
    ''')
    # create index
    cursor.execute("CREATE INDEX idx_emp_name ON employees (emp_name)")
    cursor.execute("CREATE INDEX idx_dept_name ON departments (dept_name)")

    cursor.execute("INSERT INTO departments (dept_name) VALUES ('HR')")
    cursor.execute("INSERT INTO departments (dept_name) VALUES ('IT')")
    cursor.execute("INSERT INTO departments (dept_name) VALUES ('Finance')")

    cursor.execute("INSERT INTO employees (emp_name, dept_id) VALUES ('John Doe', 1)")
    cursor.execute("INSERT INTO employees (emp_name, dept_id) VALUES ('Jane Smith', 2)")
    cursor.execute("INSERT INTO employees (emp_name, dept_id) VALUES ('Mike Johnson', 1)")
    cursor.execute("INSERT INTO employees (emp_name, dept_id) VALUES ('Emily Brown', 3)")

    conn.commit()

    cursor.execute("SELECT * FROM departments")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM employees")
    print(cursor.fetchall())

    print("Employees and their departments:")
    cursor.execute("SELECT employees.emp_name, departments.dept_name FROM employees JOIN departments ON employees.dept_id = departments.dept_id")
    print(cursor.fetchall())

    cursor.execute('''SELECT emp_id, emp_name, dept_id FROM employees''')
    print(cursor.fetchall())

    cursor.execute('''SELECT employees.emp_name, departsments.dept_name from employees JOIN departments ON employees.dept_id = departments.dept_id''')
    print(cursor.fetchall())



except Exception as e:
    print(e)
    
    
# ##############################################################################
# OUTPUT
# [(1, 'HR'), (2, 'IT'), (3, 'Finance')]
# [(1, 'John Doe', 1), (2, 'Jane Smith', 2), (3, 'Mike Johnson', 1), (4, 'Emily Brown', 3)]
# Employees and their departments:
# [('John Doe', 'HR'), ('Jane Smith', 'IT'), ('Mike Johnson', 'HR'), ('Emily Brown', 'Finance')]
# [(1, 'John Doe', 1), (2, 'Jane Smith', 2), (3, 'Mike Johnson', 1), (4, 'Emily Brown', 3)]
# no such column: departsments.dept_name